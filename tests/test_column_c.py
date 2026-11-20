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
    assert c.columnName == 'Test'
    assert c.reportColumnQueryId == 'X'
    assert c.derivedColumn == 'A'
    assert c.type == 'plainText'

