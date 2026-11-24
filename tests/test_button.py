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


def test_button_server_side_condition(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
        serverSideCondition {
            type: itemIsNull
            item: P7_ID
        }
    )
""")

    assert isinstance(b, Button)
    assert b.serverSideCondition.type == 'itemIsNull'
    assert b.serverSideCondition.item == 'P7_ID'

        