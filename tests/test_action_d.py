from apexparser import *


def test_action_d_0(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
    )
""")

    assert isinstance(a, Action)


def test_action_d_properties(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        type: title
        label: panic
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.type == 'title'
    assert a.label == 'panic'


def test_action_d_layout(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        layout {
            position: primary
            sequence: 10
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.layout.position == 'primary'
    assert a.layout.sequence == 10

def test_action_d_appearance(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        appearance {
            displayType: text
            icon: fa-home
            hot: true
            cssClasses: warning
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.appearance.displayType == 'text'
    assert a.appearance.icon == 'fa-home'
    assert a.appearance.hot == True
    assert a.appearance.cssClasses == ['warning']
