from apexparser import *


def test_action_0(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
    )
""")

    assert isinstance(a, Action)


def test_action_properties(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic
        position: title
        template: template-name
        label: panic
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.name == 'title'
    assert a.action == 'panic'
    assert a.position == 'title'
    assert a.template == 'template-name'
    assert a.label == 'panic'


def test_action_affected_elements(apex_parser):
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

    assert a.affectedElements.selectionType == 'items'
    assert a.affectedElements.region == '@/ref'
    assert a.affectedElements.columns == ['AAA']
    assert a.affectedElements.button == '@/button'
    assert a.affectedElements.items == ['P101_PASSWORD']
    assert a.affectedElements.domObject == 'div'
    assert a.affectedElements.jquerySelector == '$()'
    assert a.affectedElements.javaScriptExpression == "```javascript\nconsole.log('test')\n```"


def test_action_appearance(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        appearance {
            displayType: text
            icon: fa-home
            hot: true
            showAsDisabled: false
            cssClasses: warning
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.appearance.displayType == 'text'
    assert a.appearance.icon == 'fa-home'
    assert a.appearance.hot == True
    assert a.appearance.showAsDisabled == False
    assert a.appearance.cssClasses == ['warning']


def test_action_behavior(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        behavior {
            type: redirectOtherApp
            target: {
                    page: 36
                    items: {
                        P36_TRANSACTION_ENTRY_ID: &ID.
                    }
                    clearCache: 36
                    action: resetPagination
            }
            targetUrl: url
            linkAttributes: something
        }
    )
""")
    
    assert isinstance(a, Action)
    assert a.behavior.type == 'redirectOtherApp'
    assert a.behavior.target['page'] == 36


def test_action_execution(apex_parser):
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

    assert a.execution.sequence == 10
    assert a.execution.fireWhenEventResultIs == 'something'
    assert a.execution.fireOnInit == False
    assert a.execution.stopExecutionOnError == True
    assert a.execution.waitForResult == False


def test_action_layout(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        position: title
        template: template-name
        label: panic

        layout {
            sequence: 10
            position: primary
        }
    )
""")
    
    assert isinstance(a, Action)
    
    assert a.layout.sequence == 10
    assert a.layout.position == 'primary'


def test_action_settings(apex_parser):
    a: Action = apex_parser.parse(
"""action A (
        name: title
        action: panic

        settings {
            type: sqlQuery
            sqlQuery: select msrp from OOW_DEMO_items where id = :P3_ADD_ID;
            itemsToSubmit: P3_ADD_ID
            plsqlCode:
                ```plsql
                ```
        }
    )
""")
    
    assert isinstance(a, Action)

    assert a.settings.type == 'sqlQuery'
    assert a.settings.sqlQuery == 'select msrp from OOW_DEMO_items where id = :P3_ADD_ID;'
    assert a.settings.itemsToSubmit == ['P3_ADD_ID']
    assert a.settings.plsqlCode == '```plsql\n```'
    