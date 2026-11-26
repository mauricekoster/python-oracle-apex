from apexparser import *


def test_column_b_0(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
    )
""")

    assert isinstance(c, Column)

def test_column_b_properties(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        columnName: Test
        type: something
    )
""")

    assert isinstance(c, Column)
    assert c.columnName == 'Test'
    assert c.type == 'something'


def test_column_b_layout(apex_parser):
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


def test_column_b_appearance(apex_parser):
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


def test_column_b_source(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        source {
            primaryKey: true
            dataType: timestampWithLocalTimeZone
            availableOnClient: false
            valueProtected: true
            timezoneAware: yes
        }
    )
""")

    assert isinstance(c, Column)
    assert c.source.primaryKey == True
    assert c.source.dataType == 'timestampWithLocalTimeZone'
    assert c.source.availableOnClient == False
    assert c.source.valueProtected == True
    assert c.source.timezoneAware == 'yes'

def test_column_b_heading(apex_parser):
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
    assert c.variant == 'column_b'
    assert c.heading.heading == 'Average Sales per Store'
    assert c.heading.alignment == 'end'