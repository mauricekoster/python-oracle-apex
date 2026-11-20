from apexparser import *

def test_facet_0(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
    )
""")

    assert isinstance(f, Facet)

def test_facet_properties(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        name: abc
        type: xyz
    )
""")

    assert isinstance(f, Facet)
    assert f.name == 'abc'
    assert f.type == 'xyz'


def test_facet_label(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        label {
            label: my-label
            showLabelForCurrentFacet: true
        }
    )
""")

    assert isinstance(f, Facet)
    assert f.label.label == 'my-label'
    assert f.label.showLabelForCurrentFacet == True


def test_facet_lov(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        lov {
            type: distinctValues
        }
    )
""")

    assert isinstance(f, Facet)
    assert f.lov.type == 'distinctValues'


def test_facet_layout(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        layout {
            sequence: 40
        }
    )
""")

    assert isinstance(f, Facet)
    assert f.layout.sequence == 40


def test_facet_list_entries(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        listEntries {
            maxDisplayedEntries: 7
        }
    )
""")

    assert isinstance(f, Facet)
    assert f.list_entries.maxDisplayedEntries == 7


def test_facet_source(apex_parser):
    f: Facet = apex_parser.parse(
"""facet A (
        source {
            databaseColumn: THE_MONTH
        }
    )
""")

    assert isinstance(f, Facet)
    assert f.source.databaseColumn == 'THE_MONTH'               