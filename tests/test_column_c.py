from apexparser import *


def test_column_c_0(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
    )
""")

    assert isinstance(c, Column)

def test_column_c_properties(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText
    )
""")

    assert isinstance(c, Column)
    assert c.variant == 'column_c'

    assert c.columnName == 'Test'
    assert c.reportColumnQueryId == 'X'
    assert c.derivedColumn == 'A'
    assert c.type == 'plainText'


def test_column_c_layout(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText

        layout {
            sequence: 20
            columnAlignment: center
        }
    )
""")

    assert isinstance(c, Column)
    assert c.variant == 'column_c'
    assert c.layout.sequence == 20
    assert c.layout.columnAlignment == 'center'


def test_column_c_appearance(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText

        appearance {
            formatMask: 999G999G999G999G999G990D00
            backgroundColor: #000000
            foregroundColor: #ffffff
            barWidth: 10
            width: 99
            height: 11
            viewFileAs: inline
            template: @/template
            downloadText: download text
        }
    )
""")

    assert isinstance(c, Column)
    assert c.variant == 'column_c'

    assert c.appearance.formatMask == '999G999G999G999G999G990D00'
    assert c.appearance.backgroundColor == '#000000'
    assert c.appearance.foregroundColor == '#ffffff'
    assert c.appearance.barWidth == 10
    assert c.appearance.width == 99
    assert c.appearance.height == 11
    assert c.appearance.viewFileAs == 'inline'
    assert c.appearance.template == '@/template'
    assert c.appearance.downloadText == 'download text'


def test_column_c_heading(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText

        heading {
            heading: Suggested Price
            alignment: end
        }
    )
""")

    assert isinstance(c, Column)
    assert c.variant == 'column_c'

    assert c.heading.heading == 'Suggested Price'
    assert c.heading.alignment == 'end'


def test_column_c_sorting(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText

        sorting {
            defaultSequence: 1
            direction: desc
            sortable: false
        }
    )
""")
    
    assert isinstance(c, Column)
    assert c.variant == 'column_c'
    assert c.sorting.defaultSequence == '1'
    assert c.sorting.direction == 'desc'
    assert c.sorting.sortable == False


def test_column_c_link(apex_parser):
    c: Column = apex_parser.parse(
"""column C (
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText

        link {
            target: {
                page: 18
                items: {
                    P18_ID: #PRODUCT_ID#
                }
                clearCache: 18
                action: resetPagination
            }
            linkText: #PRODUCT#
            linkAttributes: attrs
        }
    )
""")

    assert isinstance(c, Column)
    assert c.variant == 'column_c'

    assert c.link.target['page'] == 18
    assert c.link.linkText == '#PRODUCT#'
    assert c.link.linkAttributes == 'attrs'