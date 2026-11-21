from apexparser import *


def test_computation_a_properties(apex_parser):
    c: Computation = apex_parser.parse(
"""computation A (
    )
""")

    assert isinstance(c, Computation)


def test_computation_a_properties(apex_parser):
    c: Computation = apex_parser.parse(
"""computation A (
        itemName: name
    )
""")

    assert isinstance(c, Computation)
    assert c.itemName == 'name'


def test_computation_a_execution(apex_parser):
    c: Computation = apex_parser.parse(
"""computation A (
        itemName: name

        execution {
            sequence: 10
            point: beforeHeader
        }
    )
""")

    assert isinstance(c, Computation)
    assert c.itemName == 'name'

    assert c.execution.sequence == 10
    assert c.execution.point == 'beforeHeader'


def test_computation_a_computation(apex_parser):
    c: Computation = apex_parser.parse(
"""computation A (
        itemName: name

        computation {
            sqlQuery:
                ```sql
                select * from DUAL
                ```
        }
    )
""")

# TODO:
# type
# staticValue
# computationProcessed
# language
# sqlExpression
# plsqlExpression
# javaScriptExpression
# plsqlFunctionBody
# javaScriptFunctionBody
# itemName
# preference


    assert isinstance(c, Computation)
    assert c.itemName == 'name'

    assert c.computation.sqlQuery == '```sql\nselect * from DUAL\n```'
