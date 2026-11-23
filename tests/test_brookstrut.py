from apexparser import *


def test_page_p00001():
    p = parse_apex_file("examples/brookstrut/pages/p00001-home.apx")
    assert p.name == "Home"

def test_page_p00002():
    p = parse_apex_file("examples/brookstrut/pages/p00002-sales-history-content-row.apx")
    assert p.name == "Sales History Content Row"

def test_page_p00003():
    p = parse_apex_file("examples/brookstrut/pages/p00003-store-performance.apx")
    assert p.name == "Store"

def test_page_p00004():
    p = parse_apex_file("examples/brookstrut/pages/p00004-settings.apx")
    assert p.name == "Administration"

def test_page_p00005():
    p = parse_apex_file("examples/brookstrut/pages/p00005-sales.apx")
    assert p.name == "Sales"

def test_page_p00006():
    p = parse_apex_file("examples/brookstrut/pages/p00006-stores-report-content-row.apx")
    assert p.name == "Administration"

def test_page_p00007():
    p = parse_apex_file("examples/brookstrut/pages/p00007-store.apx")
    assert p.name == "Administration"

def test_page_p00008():
    p = parse_apex_file("examples/brookstrut/pages/p00008-store-regions.apx")
    assert p.name == "Administration"

def test_page_p00009():
    p = parse_apex_file("examples/brookstrut/pages/p00009-region.apx")
    assert p.name == "Administration"

def test_page_p00011():
    p = parse_apex_file("examples/brookstrut/pages/p00011-products.apx")
    assert p.name == "Administration"

def test_page_p00012():
    p = parse_apex_file("examples/brookstrut/pages/p00012-product.apx")
    assert p.name == "Administration"

def test_page_p00013():
    p = parse_apex_file("examples/brookstrut/pages/p00013-sales-history-classic.apx")
    assert p.name == "Administration"

def test_page_p00014():
    p = parse_apex_file("examples/brookstrut/pages/p00014-about.apx")
    assert p.name == "Administration"

def test_page_p00015():
    p = parse_apex_file("examples/brookstrut/pages/p00015-region-stores.apx")
    assert p.name == "Administration"

def test_page_p00101():
    p = parse_apex_file("examples/brookstrut/pages/p00101-login.apx")
    assert p.name == "Login"

def test_page_p10010():
    p = parse_apex_file("examples/brookstrut/pages/p10010-theme-style-selection.apx")
    assert p.name == "Login"

def test_page_p10020():
    p = parse_apex_file("examples/brookstrut/pages/p10020-configuration-options.apx")
    assert p.name == "Login"    