# nicegui-command-palette

This plugin adds a command palette for NiceGUI applications.

## Installation

```sh
pip install nicegui-command-palette
```

## Usage

Register commands to the `CommandPalette` as a list of either strings or `Command` objects.

A `Command` can have a callback attached, which could be cleaner than checking the `CommandPalette`'s result.

Open the `CommandPalette` by `await`ing it. The returned value is the name of the command selected by the user, or `None` if they dismissed the palette without selecting anything.

```py
from command_palette import CommandPalette, Command

def some_action():
    ui.notify('User picked the third option!')

commands = [
    'one',
    Command('two', 'Second'),
    Command('three', 'Third', cb=some_action),
]

if result := await CommandPalette(commands):
    # result is the name of the user's selection, or None
    ui.notify(f'Selected: {result}')
```

Full example:
```py
from nicegui import ui
from nicegui.events import KeyEventArguments
from command_palette import CommandPalette, Command

async def handle_key(e: KeyEventArguments):
    # open the command palette when the user presses ctrl+shift+p
    if e.action.keydown and e.modifiers.ctrl and e.modifiers.shift and e.key == 'P':
        commands = [
            'one',
            Command('two', 'Second'),
            Command('three', 'Third', cb=some_action),
        ]
        if result := await CommandPalette(commands):
            ui.notify(result)

ui.keyboard(on_key=handle_key)

ui.run()
```

# Screenshots
![screenshot](screenshots/palette_open.png)
![usage](screenshots/usage.gif)

# Todo

- highlighting substring matches like in VSCode
- additional functions like specific prompts?
- improve matching algorithm
- figure out how to use the user fixture with dialogs