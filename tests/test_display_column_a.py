from apexparser import *


def test_display_column_a_0(apex_parser):
    d = apex_parser.parse(
"""displayColumn A (
    )
""")

    assert isinstance(d, DisplayColumn)


def test_display_column_a_properties(apex_parser):
    d = apex_parser.parse(
"""displayColumn A (
        sequence: 10
    )
""")

    assert isinstance(d, DisplayColumn)
    assert d.sequence == 10


def test_display_column_a_identification(apex_parser):
    d = apex_parser.parse(
"""displayColumn A (
        sequence: 10
        identification {
            column: AAA
        }
    )
""")

    assert isinstance(d, DisplayColumn)
    assert d.sequence == 10
    assert d.identification.column == 'AAA'
