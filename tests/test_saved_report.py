from apexparser import *


def test_saved_report_0(apex_parser):
    s = apex_parser.parse(
"""savedReport A (
    )
""")

    assert isinstance(s, SavedReport)

def test_saved_report_properties(apex_parser):
    s = apex_parser.parse(
"""savedReport A (
        visibility: primaryDefault
        name: Test
        staticId: ID
    )
""")

    assert isinstance(s, SavedReport)
    assert s.visibility == 'primaryDefault'
    assert s.name == 'Test'
    assert s.staticId == 'ID'


def test_saved_report_description(apex_parser):
    s = apex_parser.parse(
"""savedReport A (
        description {
            description:
                ```
                Hello world!
                ```
        }
    )
""")

    assert isinstance(s, SavedReport)
    assert s.description.description == "```\nHello world!\n```"


def test_saved_report_view(apex_parser):
    s = apex_parser.parse(
"""savedReport A (
        view {
           chart: false
           groupBy: false
           pivot: false
           default: AAA
           rowsPerPage: all
           stretchColumns: true
           settingsAreaExpanded: true
        }
    )
""")

    assert isinstance(s, SavedReport)
    assert s.view.chart == False
    assert s.view.groupBy == False
    assert s.view.pivot == False
    assert s.view.default == 'AAA'
    assert s.view.rowsPerPage == 'all'
    assert s.view.stretchColumns == True
    assert s.view.settingsAreaExpanded == True
    

def test_saved_report_single_row_view(apex_parser):
    s = apex_parser.parse(
"""savedReport B (
    singleRowView {
        excludeNullValues: true
        displayedColumns: true
    }

)
""")

    assert isinstance(s, SavedReport)

    assert s.singleRowView.excludeNullValues == True
    assert s.singleRowView.displayedColumns == True

