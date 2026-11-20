from apexparser import *


def test_dynamic_action_0(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
    )
""")

    assert isinstance(d, DynamicAction)

def test_dynamic_action_properties(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        name: on navigation click
    )
""")

    assert isinstance(d, DynamicAction)
    
    assert d.name == "on navigation click"

def test_dynamic_action_execution(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        execution {
            sequence: 10
        }
    )
""")

# TODO:
# eventScope
# staticContainer
# type
# time
# immediate

    assert isinstance(d, DynamicAction)
    assert d.execution.sequence == 10


def test_dynamic_action_when(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        when {
            selectionType: items
            items: P2_NAVIGATION
        }
    )
""")

# TODO:

    assert isinstance(d, DynamicAction)
    d.when.selectionType == 'items'
    d.when.items == ['P2_NAVIGATION']
