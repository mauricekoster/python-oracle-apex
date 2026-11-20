from apexparser import *


def test_action_e_0(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
    )
""")

    assert isinstance(a, Action)


def test_action_e_properties(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.position == 'title'
    assert a.template == 'template-name'
    assert a.label == 'panic'


def test_action_e_layout(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        layout {
            sequence: 10
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.layout.sequence == 10

def test_action_e_appearance(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        appearance {
            displayType: text
            icon: fa-home
            hot: true
            showAsDisabled: false
            cssClasses: warning
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.appearance.displayType == 'text'
    assert a.appearance.icon == 'fa-home'
    assert a.appearance.hot == True
    assert a.appearance.showAsDisabled == False
    assert a.appearance.cssClasses == ['warning']

def test_action_e_behavior(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        behavior {
            type: redirectOtherApp
            target: {
                    page: 36
                    items: {
                        P36_TRANSACTION_ENTRY_ID: &ID.
                    }
                    clearCache: 36
                    action: resetPagination
            }
            targetUrl: url
            linkAttributes: something
        }
    )
""")
    
    assert isinstance(a, Action)
    assert a.behavior.type == 'redirectOtherApp'
    assert a.behavior.target['page'] == 36
