from apexparser import *


def test_dynamic_action_0(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
    )
""")

    assert isinstance(d, DynamicAction)

def test_dynamic_action_properties(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        name: on navigation click
    )
""")

    assert isinstance(d, DynamicAction)
    
    assert d.name == "on navigation click"

def test_dynamic_action_execution(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        execution {
            sequence: 10
        }
    )
""")

# TODO:
# eventScope
# staticContainer
# type
# time
# immediate

    assert isinstance(d, DynamicAction)
    assert d.execution.sequence == 10


def test_dynamic_action_when(apex_parser):
    d = apex_parser.parse(
"""dynamicAction A (
        when {
            event: AAA
            customEvent: BBB
            selectionType: items
            region: @/ref
            interactiveGrid: @interactive
            columns: CCC
            button: @button
            items: P2_NAVIGATION
            domObject: DDD
            jquerySelector: EEE
            javaScriptExpression:
                ```js
                ```
        }
    )
""")

    assert isinstance(d, DynamicAction)
    d.when.event == 'AAA'
    d.when.customEvent == 'BBB'
    d.when.selectionType == 'items'
    d.when.region == '@/ref'
    d.when.interactiveGrid == '@interactive'
    d.when.columns == ['CCC']
    d.when.button == '@button'
    d.when.items == ['P2_NAVIGATION']
    d.when.domObject == 'DDD'
    d.when.jquerySelector == 'EEE'
    d.when.javaScriptExpression == '```js\n```'

