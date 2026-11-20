from apexparser import *


def test_page_item_0(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
    )
""")

    assert isinstance(p, PageItem)

def test_page_item_properties(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        name: Name
        type: Type
    )
""")

    assert isinstance(p, PageItem)
    assert p.name == 'Name'
    assert p.type == 'Type'

def test_page_item_label(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        label {
            label: Navigation
            alignment: left
        }
    )
""")

# TODO:
# tableCellAttributes

    assert isinstance(p, PageItem)
    assert p.label.label == 'Navigation'
    assert p.label.alignment == 'left'


def test_page_item_lov(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        lov {
            type: sharedComponent
            lov: @sales-history-navigation
            displayNullValue: false
        }
    )
""")

# TODO:
# sqlQuery
# staticValues
# language
# plsqlFunctionBody
# javaScriptFunctionBody
# displayExtraValues
# nullDisplayValue
# nullReturnValue

    assert isinstance(p, PageItem)
    assert p.lov.type == 'sharedComponent'
    assert p.lov.lov == '@sales-history-navigation'
    assert p.lov.displayNullValue == False
    


def test_page_item_appearance(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        appearance {
            template: @/hidden
            templateOptions: #DEFAULT#
            height: 1
        }
    )
""")

# TODO:
# cssClasses
# icon
# formatMask
# valuePlaceholder
# width

    assert isinstance(p, PageItem)
    assert p.appearance.template == '@/hidden'
    assert p.appearance.templateOptions == ['#DEFAULT#']
    assert p.appearance.height == 1


def test_page_item_default(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        default {
            type: static
            staticValue: &APP_PAGE_ID.
        }
    )
""")

    assert isinstance(p, PageItem)
    assert p.default.type == 'static'
    assert p.default.staticValue == '&APP_PAGE_ID.'
