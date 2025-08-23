
import pytest
from day1 import get_title,get_current_url


def test_title():
    url = "https://stepupandlearn.in/admission-enquiry/"
    assert get_title(url),'failed due to title is matched'

def test_get_current_url():
    url = "https://stepupandlearn.in/admission-enquiry/"
    assert get_current_url(url),'failed due to current url'