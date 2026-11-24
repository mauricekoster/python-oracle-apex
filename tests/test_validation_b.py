from apexparser import *


def test_validation_b_0(apex_parser):
    v = apex_parser.parse(
"""validation B (
    )
""")

    assert isinstance(v, Validation)

def test_validation_b_properties(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
    )
""")

    assert isinstance(v, Validation)
    assert v.name == 'P7_STORE_ADDRESS Not Null'
