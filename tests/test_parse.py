from apexparser import *

def test_parse_str(apex_parser):
    p = parse_apex("""page A (
        name: Login
    )
""")

    assert p.name == "Login"
