from pathlib import Path
from apexparser import parse_page_file

def test_file_path():
    p = parse_page_file(Path("examples/f000_page_9999.yaml"))

    assert p.name == "Login Page"

