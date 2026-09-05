import pytest
from python_oracle_apex.parser import ApexParser


@pytest.fixture(scope='package')
def apex_parser():
    return ApexParser()
