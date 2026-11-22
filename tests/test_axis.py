from apexparser import *


def test_axis_0(apex_parser):
    a = apex_parser.parse(
"""axis A (
    )
""")

    assert isinstance(a, Axis)


def test_axis_properties(apex_parser):
    a = apex_parser.parse(
"""axis A (
        name: Hello
        showAxis: true
        title: Title
    )
""")

    assert isinstance(a, Axis)
    assert a.name == 'Hello'
    assert a.showAxis == True
    assert a.title == 'Title'
