import pytest
from helper_os import *
from log_os import logger


def test_delete_api():
    obj=Helper()
    logger.info('helper object is created')
    assert obj.delete_api_status_code(),'Failed due to status code'

