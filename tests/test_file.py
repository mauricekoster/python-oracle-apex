from python_oracle_apex import *
from pathlib import Path

def test_file_str(apex_parser):
    p = apex_parser.parse_file("examples/test.apx")

    assert p.name == "Login"

def test_file_path(apex_parser):
    p = apex_parser.parse_file(Path("examples/test.apx"))

    assert p.name == "Login"