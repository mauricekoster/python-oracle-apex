from python_oracle_apex import *


def test_page_1():
    p = parse_apex_file("examples/brookstrut_page_1.apx")

    assert p.name == "Home"

def test_page_101():
    p = parse_apex_file("examples/brookstrut_page_101.apx")

    assert p.name == "Login"