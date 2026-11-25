from apexparser import *


def test_validation_b_0(apex_parser):
    v = apex_parser.parse(
"""validation B (
    )
""")

    assert isinstance(v, Validation)

def test_validation_b_properties(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
    )
""")

    assert isinstance(v, Validation)
    assert v.variant == 'validation_b'
    assert v.name == 'P7_STORE_ADDRESS Not Null'

def test_validation_b_execution(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
        execution {
            sequence: 20
        }
    )
""")

    assert isinstance(v, Validation)
    assert v.variant == 'validation_b'
    assert v.execution.sequence == 20

def test_validation_b_validation(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
        validation {
            type: functionBodyReturningBoolean
            plsqlFunctionBody: return trim(:P7_STORE_ADDRESS) is not null
        }
    )
""")

# TODO: validation

    assert isinstance(v, Validation)
    assert v.variant == 'validation_b'

    assert v.validation.type == 'functionBodyReturningBoolean'
    assert v.validation.plsqlFunctionBody == 'return trim(:P7_STORE_ADDRESS) is not null'


def test_validation_b_error(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
        error {
            errorMessage: #LABEL# must have some value.
            displayLocation: inlineWithField
            associatedItem: @P7_STORE_ADDRESS
            associatedColumn: CCC
        }
    )
""")

    assert isinstance(v, Validation)
    assert v.variant == 'validation_b'

    assert v.error.errorMessage == '#LABEL# must have some value.'
    assert v.error.displayLocation == 'inlineWithField'
    assert v.error.associatedItem == '@P7_STORE_ADDRESS'
    assert v.error.associatedColumn == 'CCC'


def test_validation_b_server_side_condition(apex_parser):
    v = apex_parser.parse(
"""validation B (
        name: P7_STORE_ADDRESS Not Null
        serverSideCondition {
            type: requestIsContainedInValue
            value: CREATE,SAVE
        }
    )
""")

# TODO: serverSideCondition

    assert isinstance(v, Validation)
    assert v.variant == 'validation_b'

    assert v.serverSideCondition.type == 'requestIsContainedInValue'
    assert v.serverSideCondition.value == 'CREATE,SAVE'
