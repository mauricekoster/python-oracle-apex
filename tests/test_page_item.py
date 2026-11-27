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
            displayNullValue: true
            nullDisplayValue: - Select Value -
            sqlQuery:
                ```sql
                ```
        }
    )
""")

# TODO:
# staticValues
# language
# plsqlFunctionBody
# javaScriptFunctionBody
# displayExtraValues
# nullReturnValue

    assert isinstance(p, PageItem)
    assert p.lov.type == 'sharedComponent'
    assert p.lov.lov == '@sales-history-navigation'
    assert p.lov.displayNullValue == True
    assert p.lov.nullDisplayValue == '- Select Value -'
    assert p.lov.sqlQuery == '```sql\n```'


def test_page_item_appearance(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        appearance {
            template: @/hidden
            templateOptions: #DEFAULT#
            height: 1
            formatMask: DD-MON-YYYY
            width: 64
        }
    )
""")

# TODO:
# cssClasses
# icon
# valuePlaceholder

    assert isinstance(p, PageItem)
    assert p.appearance.template == '@/hidden'
    assert p.appearance.templateOptions == ['#DEFAULT#']
    assert p.appearance.height == 1
    assert p.appearance.width == 64
    assert p.appearance.formatMask == 'DD-MON-YYYY'


def test_page_item_default(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        default {
            type: static
            staticValue: &APP_PAGE_ID.
            sqlQuerySingleValue: select sysdate from dual
        }
    )
""")

# TODO: default    

    assert isinstance(p, PageItem)
    assert p.default.type == 'static'
    assert p.default.staticValue == '&APP_PAGE_ID.'
    assert p.default.sqlQuerySingleValue == 'select sysdate from dual'

def test_page_item_source(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        source {
            type: databaseColumn
            databaseColumn: ID
            used: always
            plsqlFunctionBody:
                ```plsql
                ```
        }
    )
""")

    assert isinstance(p, PageItem)
    assert p.source.type == 'databaseColumn'
    assert p.source.databaseColumn == 'ID'
    assert p.source.used == 'always'
    assert p.source.plsqlFunctionBody == '```plsql\n```'


def test_page_item_layout(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        layout {
            sequence: 10
            region: @store
            slot: regionBody
            startNewRow: false
        }
    )
""")

# TODO: layout

    assert isinstance(p, PageItem)  
    assert p.layout.sequence == 10
    assert p.layout.region == '@store'  
    assert p.layout.slot == 'regionBody'
    assert p.layout.startNewRow == False
    

def test_page_item_advanced(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        advanced {
            cssClasses: mnw180
        }
    )
""")

# TODO: advanced

    assert isinstance(p, PageItem)  
    assert p.advanced.cssClasses == ['mnw180']


def test_page_item_settings(apex_parser):
    p = apex_parser.parse(
"""pageItem A (
        settings {
            trimSpaces: none
            showControls: movingOnly
            valueProtected: true
            minValue: 0
            maxValue: 100
            numberAlignment: end
            virtualKeyboard: text
        }
    )
""")


    assert isinstance(p, PageItem)  
    assert p.settings.trimSpaces == 'none'
    assert p.settings.showControls == 'movingOnly'
    assert p.settings.valueProtected == True
    assert p.settings.minValue == 0
    assert p.settings.maxValue == 100
    assert p.settings.numberAlignment == 'end'
    assert p.settings.virtualKeyboard == 'text'

