import pytest
from nicegui import ui
from nicegui.testing import Screen
from nicegui_command_palette import CommandPalette
from selenium.webdriver.common.keys import Keys


def test_palette(screen: Screen) -> None:
   
    async def show() -> None:
        cmd = CommandPalette()
        cmd.add_item('one')
        cmd.add_item('two')
        results.append(await cmd)

    results: list[str] = []
    ui.button('Open', on_click=show)

    screen.open('/')
    screen.should_contain('Open')
    screen.click('Open')
    screen.should_contain('one')
    screen.should_contain('two')



    # await user.should_see('click me')
    # user.find(ui.button).click()
    # await user.should_see('one')
    # await user.should_see('two')
    # table = user.find(ui.table).elements.pop()
    # assert table.rows[0]['value'] == 'one'
