from apexparser import *


def test_aggregate_0(apex_parser):
    a = apex_parser.parse(
"""aggregate A (
    )
""")

    assert isinstance(a, Aggregate)

def test_aggregate_properties(apex_parser):
    a = apex_parser.parse(
"""aggregate A (
        function: sum
        column: AAA
        showGrandTotal: true
        tooltip: Something usefull
    )
""")

    assert isinstance(a, Aggregate)
    assert a.function == 'sum'
    assert a.column == 'AAA'
    assert a.showGrandTotal == True
    assert a.tooltip == 'Something usefull'
    

def test_aggregate_advanced(apex_parser):
    a = apex_parser.parse(
"""aggregate B (

        advanced {
            staticId: ID
            enabled: true
        }
    )
""")

    assert isinstance(a, Aggregate)

    assert a.advanced.staticId == "ID"
    assert a.advanced.enabled == True