from apexparser import *


def test_action_c_0(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
    )
""")

    assert isinstance(a, Action)


def test_action_c_properties(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.name == 'title'
    assert a.action == 'panic'

def test_action_c_execution(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic
        execution {
            sequence: 10
            fireOnInit: false
        }
    )
""")
    
    assert isinstance(a, Action)
    assert a.execution.sequence == 10
    assert a.execution.fireOnInit == False