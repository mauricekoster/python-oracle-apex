from apexparser import *


def test_filter_c_0(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        
    )
""")

    assert isinstance(f, Filter)
    

def test_filter_c_properties(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        name: my-filter
        type: checkboxGroup
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.name == 'my-filter'
    assert f.type == 'checkboxGroup'


def test_filter_c_label(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter_c
        
        label {
            label: Test
        }
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.label.label == 'Test'


def test_filter_c_layout(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter_c
        
        layout {
            sequence: 30
        }
    )
""")

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.layout.sequence == 30


def test_filter_c_lov(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter_c
        
        lov {
            type: distinctValues
        }
    )
""")

# TODO: lov

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.lov.type == 'distinctValues'

def test_filter_c_suggestions(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter_c
        
        suggestions {
            type: dynamic
        }
    )
""")

# TODO: suggestions

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.suggestions.type == 'dynamic'


def test_filter_c_source(apex_parser):
    f: Filter = apex_parser.parse(
"""filter C (
        variant: filter_c
        
        source {
            databaseColumn: STORE
        }
    )
""")

# TODO: source

    assert isinstance(f, Filter)
    assert f.variant == 'filter_c'

    assert f.source.databaseColumn == 'STORE'
