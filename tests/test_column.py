from apexparser import *


def test_column_0(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
    )
""")

    assert isinstance(c, Column)

def test_column_properties(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        name: Test
        columnName: Test
        reportColumnQueryId: X
        derivedColumn: A
        type: plainText
    )
""")

    assert isinstance(c, Column)
    assert c.name == 'Test'
    assert c.columnName == 'Test'
    assert c.reportColumnQueryId == 'X'
    assert c.derivedColumn == 'A'
    assert c.type == 'plainText'


def test_column_advanced(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        type: plainText
        advanced {
            htmlDomId: ID
            endUserAlias: J
            cssClasses: [
                dummy
            ]
            computeSum: true
            customAttributes: something
            cellWidth: 99
        }
    )
""")

    assert isinstance(c, Column)
    assert c.advanced.htmlDomId == 'ID'
    assert c.advanced.endUserAlias == 'J'    
    assert c.advanced.cssClasses == ['dummy']
    assert c.advanced.computeSum == True
    assert c.advanced.customAttributes == 'something'
    assert c.advanced.cellWidth == 99


def test_column_appearance(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        appearance {
            cssClasses: aaa
            formatMask: start
            backgroundColor: blue
            foregroundColor: #ffffff
            barWidth: 10
            viewFileAs: inline
            downloadText: something
            width: 99
            height: 11
            template: @/template
            group: true
        }
    )
""")

    assert isinstance(c, Column)    
    assert c.appearance.cssClasses == ['aaa']
    assert c.appearance.formatMask == 'start'
    assert c.appearance.backgroundColor == 'blue'
    assert c.appearance.foregroundColor == '#ffffff'
    assert c.appearance.barWidth == 10
    assert c.appearance.viewFileAs == 'inline'
    assert c.appearance.downloadText == 'something'
    assert c.appearance.width == 99
    assert c.appearance.height == 11
    assert c.appearance.template == '@/template'
    assert c.appearance.group == True


def test_column_column_formatting(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        type: plainText
        columnFormatting {
            htmlExpression: #SALES_TREND_PERCENTAGE#%
        }
    )
""")

    assert isinstance(c, Column)
    assert c.columnFormatting.htmlExpression == '#SALES_TREND_PERCENTAGE#%'


def test_column_heading(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        type: plainText
        heading {
            heading: Average Sales per Store
            alternativeLabel: alt
            alignment: end
        }
    )
""")

    assert isinstance(c, Column)
    assert c.heading.heading == 'Average Sales per Store'
    assert c.heading.alignment == 'end'
    assert c.heading.alternativeLabel == 'alt'


def test_column_layout(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        layout {
            sequence: 10
            columnAlignment: start
            group: @group-1
        }
    )
""")

    assert isinstance(c, Column)
    c.layout.sequence == 10
    c.layout.columnAlignment == 'start'
    c.layout.group == '@group-1'



def test_column_link(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        type: plainText
        link {
            target: {
                page: 15
                items: {
                    P15_REGION_ID: #ID#
                }
                action: resetPagination
            }
            linkText: #REGION_NAME#
            linkAttributes: css
        }
    )
""")

    assert isinstance(c, Column)

    assert c.link.linkText == '#REGION_NAME#'
    assert c.link.linkAttributes == 'css'
    assert c.link.target['page'] == 15


def test_column_security(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        type: plainText
        security {
            authorizationScheme: @https
            escapeSpecialChars: true
        }
    )
""")

    assert isinstance(c, Column)
    assert c.security.authorizationScheme == '@https'
    assert c.security.escapeSpecialChars == True


def test_column_sorting(apex_parser):
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
    assert c.sorting.defaultSequence == '1'
    assert c.sorting.direction == 'desc'
    assert c.sorting.sortable == False


def test_column_source(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        source {
            primaryKey: true
            dataType: timestampWithLocalTimeZone
            availableOnClient: false
            valueProtected: true
            timezoneAware: yes
            type: databaseColumn
            databaseColumn: COLUMN1
            sqlExpression:
                ```sql
                SELECT * FROM DUAL;
                ```
        }
    )
""")

    assert isinstance(c, Column)
    assert c.source.primaryKey == True
    assert c.source.dataType == 'timestampWithLocalTimeZone'
    assert c.source.availableOnClient == False
    assert c.source.valueProtected == True
    assert c.source.timezoneAware == 'yes'
    assert c.source.type == 'databaseColumn'
    assert c.source.databaseColumn == 'COLUMN1'
    assert c.source.sqlExpression == '```sql\nSELECT * FROM DUAL;\n```'