# nicegui-command-palette

This plugin adds a command palette for NiceGUI applications.

## Installation

```sh
pip install nicegui-command-palette
```

## Usage

```py
from command_palette import CommandPalette

# create the palette
cmd = CommandPalette()
# add items
cmd.add_item('one')
cmd.add_item('two')
# then open the palette by awaiting it
result = await cmd
ui.notify(result)

# OR create your options as a list
options = ['one', 'two']
# then create the palette and immediately await it
if result := await CommandPalette(options):
    ui.notify(result)

# OR create your options as a dict
# return value: display value
options = {
    'one': 'The First Option',
    'two': 'A Second Option',
}
```

Full example:
```py
from nicegui import ui
from nicegui.events import KeyEventArguments
from command_palette import CommandPalette

async def handle_key(e: KeyEventArguments):
    if e.action.keydown and e.modifiers.shift and e.modifiers.ctrl and e.key == 'P':
 
        options = ['one', 'two']
        if result := await CommandPalette(options):
            ui.notify(result, position='bottom-right')

ui.keyboard(on_key=handle_key)

ui.run()
```

# Screenshots
![screenshot](screenshots/palette.png)
![usage](screenshots/usage.gif)

# Todo

- highlighting substring matches like in VSCode
- additional functions like specific prompts?
- improve matching algorithm