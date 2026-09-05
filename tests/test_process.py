from parsimonious import ParseError
from python_oracle_apex import *
import pytest

def test_process_0(apex_parser):
    p = apex_parser.parse(
"""process clear-page-s-cache (
    )
""")

    assert isinstance(p, Process)
    assert p.component_id == 'clear-page-s-cache'

def test_process_1(apex_parser):
    p = apex_parser.parse(
"""process clear-page-s-cache (
        name: Test
        type: something
        executionChain: exec_chain
        formRegion: @form_region
        editableRegion: @editable_region
    )
""")

    assert isinstance(p, Process)
    assert p.component_id == 'clear-page-s-cache'
    assert p.name == "Test"
    assert p.type == "something"


def test_process_2(apex_parser):

    with pytest.raises(ParseError):
        p = apex_parser.parse(
        """process clear-page-s-cache (
                wrong: something
            )
        """)


def test_process_execution(apex_parser):
    p : Process = apex_parser.parse(
        """process clear-page-s-cache (
                execution {
                    sequence: 10
                    point: something
                    runProcess: oncePerSessionOrWhenReset
                }
            )
""")
    assert p.execution.sequence == 10
    assert p.execution.point == "something"
    assert p.execution.runProcess == "oncePerSessionOrWhenReset"


def test_process_advanced(apex_parser):
    p : Process = apex_parser.parse(
    """process clear-page-s-cache (
        advanced {
            staticId: ABCDEF
            executionMappingIdentifier: 22202516004377822257
        }
    )
""")
    assert p.advanced.staticId == "ABCDEF"
    assert p.advanced.executionMappingIdentifier == "22202516004377822257"


def test_process_source_0(apex_parser):
    p : Process = apex_parser.parse(
    """process clear-page-s-cache (
        source {
            location: restEnabledSql
            language: plsql
            remoteServer: @ducktown
        }
    )
""")
    assert p.source.location == "restEnabledSql"
    assert p.source.language == "plsql"
    assert p.source.remoteServer == "@ducktown"


def test_process_source_1(apex_parser):
    p : Process = apex_parser.parse(
    """process clear-page-s-cache (
        source {
            plsqlCode: :P101_USERNAME := apex_authentication.get_login_username_cookie;
        }
    )
""")
    assert p.source.plsqlCode == ":P101_USERNAME := apex_authentication.get_login_username_cookie;"


def test_process_source_2a(apex_parser):
    p : Process = apex_parser.parse(
    """process clear-page-s-cache (
        source {
            plsqlCode: ```plsql
                apex_authentication.send_login_username_cookie (
                    p_username => lower(:P101_USERNAME) );
                ```
        }
    )
""")
    assert p.source.plsqlCode == "```plsql\napex_authentication.send_login_username_cookie (\n    p_username => lower(:P101_USERNAME) );\n```"

def test_process_source_2b(apex_parser):
    p : Process = apex_parser.parse(
    """process clear-page-s-cache (
        source {
            plsqlCode: 
                ```plsql
                apex_authentication.send_login_username_cookie (
                    p_username => lower(:P101_USERNAME) );
                ```
        }
    )
""")
    assert p.source.plsqlCode == "```plsql\napex_authentication.send_login_username_cookie (\n    p_username => lower(:P101_USERNAME) );\n```"
    