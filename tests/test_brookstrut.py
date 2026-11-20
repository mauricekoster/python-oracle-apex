from apexparser import *


def test_page():
    p = parse_apex_file("examples/brookstrut.apx")
    assert p.name == "Sales History Content Row"


def test_page_p00001():
    p = parse_apex_file("examples/brookstrut/pages/p00001-home.apx")
    assert p.name == "Home"


def test_page_p00002():
    p = parse_apex_file("examples/brookstrut/pages/p00002-sales-history-content-row.apx")
    assert p.name == "Sales History Content Row"


def test_page_p00101():
    p = parse_apex_file("examples/brookstrut/pages/p00101-login.apx")

    assert p.name == "Login"