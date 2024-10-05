from nicegui import ui
from nicegui.events import KeyEventArguments
from nicegui_command_palette import CommandPalette, Command


@ui.page('/')
def index():
    async def handle_key(e: KeyEventArguments):
        # if e.action.keydown:
        #     ui.notify(e.key, position='bottom-left', group=False)
        if e.modifiers.shift and e.modifiers.ctrl and e.action.keydown and e.key == 'P':

            commands = [
                'one',
                Command('two', 'Second'),
                Command('three', 'Third', cb=lambda: ui.notify('Picked the third option')),
            ]

            if result := await CommandPalette(commands):
                ui.notify(result, position='bottom-right')

    ui.keyboard(on_key=handle_key, ignore=[])


ui.run(
    title='Command Palette',
    uvicorn_reload_includes='*.vue',
    dark=True,
)
