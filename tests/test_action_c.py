from apexparser import *


def test_action_c_0(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
    )
""")

    assert isinstance(a, Action)


def test_action_c_properties(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic
    )
""")
    
    assert isinstance(a, Action)
    assert a.variant == 'action_c'
    
    assert a.name == 'title'
    assert a.action == 'panic'


def test_action_c_affected_elements(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic

        affectedElements {
                selectionType: items
                region: @/ref
                columns: AAA
                button: @/button
                items: P101_PASSWORD
                domObject: div
                jquerySelector: $()
                javaScriptExpression: 
                    ```javascript
                    console.log('test')
                    ```
            }
    )
""")
    
    assert isinstance(a, Action)
    assert a.variant == 'action_c'

    assert a.affectedElements.selectionType == 'items'
    assert a.affectedElements.region == '@/ref'
    assert a.affectedElements.columns == ['AAA']
    assert a.affectedElements.button == '@/button'
    assert a.affectedElements.items == ['P101_PASSWORD']
    assert a.affectedElements.domObject == 'div'
    assert a.affectedElements.jquerySelector == '$()'
    assert a.affectedElements.javaScriptExpression == "```javascript\nconsole.log('test')\n```"

def test_action_c_execution(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic
        execution {
            sequence: 10
            fireWhenEventResultIs: something
            fireOnInit: false
            stopExecutionOnError: true
            waitForResult: false
        }
    )
""")
    
    assert isinstance(a, Action)
    assert a.variant == 'action_c'

    assert a.execution.sequence == 10
    assert a.execution.fireWhenEventResultIs == 'something'
    assert a.execution.fireOnInit == False
    assert a.execution.stopExecutionOnError == True
    assert a.execution.waitForResult == False

def test_action_c_settings(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic

        settings {
            type: sqlQuery
            sqlQuery: select msrp from OOW_DEMO_items where id = :P3_ADD_ID;
            itemsToSubmit: P3_ADD_ID
        }
    )
""")
    
    assert isinstance(a, Action)
    assert a.variant == 'action_c'

    assert a.settings.type == 'sqlQuery'
    assert a.settings.sqlQuery == 'select msrp from OOW_DEMO_items where id = :P3_ADD_ID;'
    assert a.settings.itemsToSubmit == ['P3_ADD_ID']
    