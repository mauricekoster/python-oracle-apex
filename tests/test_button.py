from apexparser import *


def test_button_0(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
    )
""")

    assert isinstance(b, Button)

def test_button_behavior(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
    behavior {
        action: redirectThisApp
        warnOnUnsavedChanges: doNotCheck
        databaseAction: insert
        targetUrl: javascript:apex.confirm(htmldb_delete_message,'DELETE');
        executeValidations: false
        target: {
            page: 1
            clearCache: [ 
                6 
                XX
                AA
                RIR 
            ]
        }
    }
    )
""")

    assert isinstance(b, Button)
    assert b.behavior.action == 'redirectThisApp'
    assert b.behavior.warnOnUnsavedChanges == 'doNotCheck'
    assert b.behavior.databaseAction == 'insert'
    assert b.behavior.target['page'] == 1
    assert b.behavior.targetUrl == "javascript:apex.confirm(htmldb_delete_message,'DELETE');"
    assert b.behavior.executeValidations == False

def test_button_server_side_condition(apex_parser):
    b: Button = apex_parser.parse(
"""button A (
        serverSideCondition {
            type: itemIsNull
            item: P7_ID
        }
    )
""")

    assert isinstance(b, Button)
    assert b.serverSideCondition.type == 'itemIsNull'
    assert b.serverSideCondition.item == 'P7_ID'

        