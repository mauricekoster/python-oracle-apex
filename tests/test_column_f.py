from apexparser import *


def test_column_f_0(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
    )
""")

    assert isinstance(c, Column)

def test_column_f_properties(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        name: Test
    )
""")

    assert isinstance(c, Column)
    assert c.name == 'Test'


def test_column_f_layout(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        name: Test
        layout {
            sequence: 10
        }
    )
""")

    assert isinstance(c, Column)
    c.layout.sequence == 10


def test_column_f_appearance(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        name: Test
        appearance {
            formatMask: start
            group: true
        }
    )
""")

    assert isinstance(c, Column)    
    assert c.appearance.formatMask == 'start'
    assert c.appearance.group == True


def test_column_f_source(apex_parser):
    c: Column = apex_parser.parse(
"""column A (
        source {
            type: databaseColumn
            databaseColumn: COLUMN1
            sqlExpression:
                ```sql
                SELECT * FROM DUAL;
                ```
            dataType: sdoGeometry
            primaryKey: true
            availableOnClient: false
            valueProtected: true
        }
    )
""")

    assert isinstance(c, Column)
    assert c.source.type == 'databaseColumn'
    assert c.source.databaseColumn == 'COLUMN1'
    assert c.source.sqlExpression == '```sql\nSELECT * FROM DUAL;\n```'
    assert c.source.dataType == 'sdoGeometry'
    assert c.source.primaryKey == True
    assert c.source.availableOnClient == False
    assert c.source.valueProtected == True
    