from python_oracle_apex import *


def test_page_0(apex_parser):
    p = apex_parser.parse(
"""page A (
    )
""")

    assert isinstance(p, Page)

def test_page_1(apex_parser):
    p = apex_parser.parse(
"""page A (
        page: 1000
        name: Hallo
        alias: HOME
        title: How the West was won
    )
""")

    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.alias == "HOME"
    assert p.title == "How the West was won"


def test_page_help(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        help {
            helpText: No help is available for this page.
        }
    )
""")
    assert p.help.helpText == "No help is available for this page."
    