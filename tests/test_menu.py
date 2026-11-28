from apexparser import *


def test_menu_0(apex_parser):
    m: Menu = apex_parser.parse(
"""menu A (
    )
""")

    assert isinstance(m, Menu)

def test_menu_properties(apex_parser):
    m: Menu = apex_parser.parse(
"""menu A (
        type: separator
        label: Bananana
        parentMenu: @parent
    )
""")

    assert isinstance(m, Menu)
    assert m.variant == 'menu'

    assert m.type == 'separator'
    assert m.label == 'Bananana'
    assert m.parentMenu == '@parent'

def test_menu_layout(apex_parser):
    m: Menu = apex_parser.parse(
"""menu A (
        layout {
            sequence: 10
        }
    )
""")

    assert isinstance(m, Menu)
    assert m.variant == 'menu'

    assert m.layout.sequence == 10

def test_menu_behavior(apex_parser):
    m: Menu = apex_parser.parse(
"""menu A (
        behavior {
            type: redirectThisApp
            target: {
                page: 7
                items: {
                    P7_ID: &ID.
                }
                clearCache: 7
            }
            targetUrl: http://example.com
            linkAttributes: attrs
        }
    )
""")

    assert isinstance(m, Menu)
    assert m.variant == 'menu'
    
    assert m.behavior.type == 'redirectThisApp'
    assert type(m.behavior.target) is dict
    assert m.behavior.targetUrl == 'http://example.com'
    assert m.behavior.linkAttributes == 'attrs'
