from apexparser import *


def test_aggregate_a_0(apex_parser):
    a = apex_parser.parse(
"""aggregate A (
    )
""")

    assert isinstance(a, Aggregate)

def test_aggregate_a_properties(apex_parser):
    a = apex_parser.parse(
"""aggregate A (
        function: sum
        column: AAA
    )
""")

    assert isinstance(a, Aggregate)
    assert a.function == 'sum'
    assert a.column == 'AAA'
