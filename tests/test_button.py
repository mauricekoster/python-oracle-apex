from python_oracle_apex import *


def test_button_0(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
    )
""")

    assert isinstance(b, Button)

def test_button_behavior(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
    behavior {
        target: {
            page: 1
        }
    }
    )
""")

    assert isinstance(b, Button)
