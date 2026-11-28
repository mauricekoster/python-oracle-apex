from apexparser import *


def test_branch_0(apex_parser):
    b: Branch = apex_parser.parse(
"""branch A (
    )
""")

    assert isinstance(b, Branch)

def test_branch_properties(apex_parser):
    b: Branch = apex_parser.parse(
"""branch A (
        name: test
    )
""")

    assert isinstance(b, Branch)
    assert b.name == 'test'

def test_branch_execution(apex_parser):
    b: Branch = apex_parser.parse(
"""branch A (
        name: test
        execution {
            sequence: 40
        }
    )
""")

    assert isinstance(b, Branch)
    assert b.name == 'test'    
    assert b.execution.sequence == 40


def test_branch_behavior(apex_parser):
    b: Branch = apex_parser.parse(
"""branch A (
        name: test
        behavior {
            target: {
                page: &P2_NAVIGATION.
                clearCache: &P2_NAVIGATION.
                action: resetPagination
            }
        }
    )
""")

    assert isinstance(b, Branch)
    assert b.name == 'test'    
    assert b.behavior.target['page'] == '&P2_NAVIGATION.'