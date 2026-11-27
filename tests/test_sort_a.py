from apexparser import *


def test_sort_a_0(apex_parser):
    s = apex_parser.parse(
"""sort A (
    )
""")

    assert isinstance(s, Sort)

def test_sort_a_properties(apex_parser):
    s = apex_parser.parse(
"""sort A (
        column: AAA
    )
""")

    assert isinstance(s, Sort)
    s.column == 'AAA'

def test_sort_a_sort(apex_parser):
    s = apex_parser.parse(
"""sort A (
        column: AAA
        sort {
            direction: asc
            nulls: first
            sequence: 99
        }
    )
""")

    assert isinstance(s, Sort)
    s.sort.direction == 'asc'
    s.sort.nulls == 'first'
    s.sort.sequence == 99
    