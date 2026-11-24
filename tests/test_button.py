from apexparser import *


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
            clearCache: [ 
                6 
                XX
                AA
                RIR 
            ]
        }
    }
    )
""")

    assert isinstance(b, Button)
    assert b.behavior.target['page'] == 1