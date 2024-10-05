from nicegui import ui
from nicegui.events import GenericEventArguments, ValueChangeEventArguments
from difflib import SequenceMatcher


class CommandTable(ui.table, component='command_table.vue'):
    def __init__(self) -> None:
        columns = [
            {'name': 'value', 'label': 'value', 'field': 'value', 'align': 'left'},
            # {'name': 'ratio', 'label': 'ratio', 'field': 'ratio', 'align': 'right'},
        ]
        super().__init__(rows=[], columns=columns, row_key='id')
        self.items = []
        self.current_selection = 0

    def select_up(self):
        self.current_selection = max(self.current_selection - 1, 0)
        self.set_selection()

    def select_down(self):
        self.current_selection = min(self.current_selection + 1, len(self.items) - 1)
        self.set_selection()

    def set_selection(self):
        if self.items:
            self.selected = [self.items[self.current_selection]]

    def get_selection(self):
        return self.selected[0]['value']

    def add_item(self, value: str, label: str = None):
        row = {
            'value': value,
            'label': label if label else value,
            'id': len(self.items),
            'ratio': 1,
        }
        self.items.append(row)
        self.add_row(row)

    def sort(self, target: str):
        target = target.lower()
        for item in self.items:
            label = item['label'].lower()
            item['ratio'] = SequenceMatcher(a=label, b=target).ratio()
            if target.lower() not in label:
                item['ratio'] = 0

        if target:
            self.items.sort(key=lambda x: x['ratio'], reverse=True)
            items = filter(lambda x: x['ratio'] > 0, self.items)
        else:
            self.items.sort(key=lambda x: x['id'])
            items = self.items

        self.update_rows(items, clear_selection=False)
        self.current_selection = 0
        self.set_selection()


class Command:
    def __init__(self, name: str, label: str = None, cb=None) -> None:
        self.name = name
        self.label = label if label else name
        self.cb = cb

    def execute(self):
        if self.cb:
            self.cb()


class CommandPalette(ui.dialog):
    def __init__(self, commands: list[str | Command] = None) -> None:
        super().__init__(value=True)

        self.props('transition-duration=0')

        with self, ui.card().classes('absolute top-10 w-1/2').tight():
            self.text = ui.input(on_change=self.on_change).classes('w-full px-2')
            self.table = CommandTable()

        self.text.run_method('select')
        self.on('keydown', self.handle_key)
        self.table.on('row_clicked', self.row_clicked)

        self.commands: dict[str, Command] = {}
        if commands is not None:
            for c in commands:
                self.add_command(c)

    def on_change(self, e: ValueChangeEventArguments):
        self.table.sort(e.value)

    def row_clicked(self, e: GenericEventArguments):
        value = e.args['value']
        self.execute_command(value)

    def add_command(self, command: str | Command, label: str = None, cb=None):
        if isinstance(command, str):
            command = Command(command, label, cb)

        self.table.add_item(command.name, command.label)

        self.commands[command.name] = command

    def execute_command(self, name: str):
        if cmd := self.commands.get(name, None):
            cmd.execute()

        self.submit(name)

    def handle_key(self, e: GenericEventArguments):
        if e.args['key'] == 'Enter':
            self.execute_command(self.table.get_selection())
        if e.args['key'] == 'ArrowUp':
            self.table.select_up()
        if e.args['key'] == 'ArrowDown':
            self.table.select_down()

    def __await__(self):
        self.table.set_selection()

        items = [c.label for c in self.commands.values()]
        self.text.set_autocomplete(items)

        return super().__await__()
