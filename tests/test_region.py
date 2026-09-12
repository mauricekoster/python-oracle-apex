from python_oracle_apex import *


def test_region_0(apex_parser):
    r = apex_parser.parse(
"""region A (
    )
""")

    assert isinstance(r, Region)


def test_region_source(apex_parser):
    r = apex_parser.parse(
"""region A (
        source {
            list: @application-actions
        }
    )
""")

    assert isinstance(r, Region)
