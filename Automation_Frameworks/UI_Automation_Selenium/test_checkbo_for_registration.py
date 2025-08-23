import pytest
from day4 import click_on_radio_button
from constant import list_of_options





@pytest.mark.skip
def test_check_python_menu():
    for i in list_of_options:
        assert click_on_radio_button(i),'failed to select python'

@pytest.mark.skip
def test_check_java_menu():
    assert click_on_radio_button(list_of_options[1]),'failed to select java'

@pytest.mark.skip
def test_check_php_menu():
    assert click_on_radio_button(list_of_options[2]),'failed to select php'

@pytest.mark.skip
def test_check_nodejs_menu():
    assert click_on_radio_button(list_of_options[3]),'failed to select nodejs'







@pytest.mark.skip
def test_check_box1():
    assert check_box(male=True,female=False),'failed to click on male locator'
@pytest.mark.skip
def test_check_box2():
    assert check_box(male=False,female=True),'failed to click on male locator'