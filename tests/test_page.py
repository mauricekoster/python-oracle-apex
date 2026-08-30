from python_oracle_apex import *


def test_page_0():
    p = parse_apex(
"""page A (
    )
""")

    assert isinstance(p, Page)

def test_page_1():
    p = parse_apex(
"""page A (
        name: Hallo
    )
""")

    assert isinstance(p, Page)
    assert p.name == "Hallo"


def test_file():
    p = parse_apex_file("examples/test.apx")

    assert p.name == "Login"