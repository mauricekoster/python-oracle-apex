import pytest
from apexparser.parser import ApexParser


@pytest.fixture(scope='package')
def apex_parser():
    return ApexParser()
