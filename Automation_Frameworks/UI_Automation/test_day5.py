from day5 import search_data_in_google
import pytest


def test_facebook():
    assert search_data_in_google('facebook'),'failed due to facebook search'

def test_search_with_special_char():
    assert search_data_in_google('$%#@&*'),'failed due to $%#@&* search'

def test_seach_space():
    assert search_data_in_google(' '),'failed due to space search'

def test_search_numbers():
    assert search_data_in_google('98765456'),'failed due to 98765456 search'

def test_marathi_char():
    assert search_data_in_google('पूर्ण विराम'),'failed due to पूर्ण विराम search'

def test_chanise_char():
    assert search_data_in_google('象形; xiàngxíng'),'failed due to 象形; xiàngxíng search'

def test_chanise_emoji():
    assert search_data_in_google('😃💁'),'failed due to 😃💁  search'