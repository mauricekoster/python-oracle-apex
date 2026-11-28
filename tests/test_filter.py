from apexparser import *


def test_filter_0(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        
    )
""")

    assert isinstance(f, Filter)
    

def test_filter_properties(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        name: my-filter
        type: checkboxGroup
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.name == 'my-filter'
    assert f.type == 'checkboxGroup'


def test_filter_label(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter
        
        label {
            label: Test
        }
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.label.label == 'Test'


def test_filter_layout(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter
        
        layout {
            sequence: 30
        }
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.layout.sequence == 30


def test_filter_lov(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter
        
        lov {
            type: distinctValues
        }
    )
""")

# TODO: lov

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.lov.type == 'distinctValues'

def test_filter_suggestions(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter
        
        suggestions {
            type: dynamic
        }
    )
""")

# TODO: suggestions

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.suggestions.type == 'dynamic'


def test_filter_source(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter
        
        source {
            databaseColumn: STORE
        }
    )
""")

# TODO: source

    assert isinstance(f, Filter)
    assert f.variant == 'filter'

    assert f.source.databaseColumn == 'STORE'
