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

def test_axis_value(apex_parser):
    a = apex_parser.parse(
"""axis A (
        value {
            min: 3
            max: 99
            format: decimal
            decimalPlaces: 0
            currency: eur
            pattern: ###.##
            formatScaling: none
            baselineScaling: min
            scale: log
            step: 3
        }
    )
""")

    assert isinstance(a, Axis)
    assert a.value.min == 3
    assert a.value.max == 99
    assert a.value.format == 'decimal'
    assert a.value.decimalPlaces == 0
    assert a.value.currency == 'eur'
    assert a.value.pattern == '###.##'
    assert a.value.formatScaling == 'none'
    assert a.value.baselineScaling == 'min'
    assert a.value.scale == 'log'
    assert a.value.step == 3

def test_axis_minor_ticks(apex_parser):
    a = apex_parser.parse(
"""axis A (
        minorTicks {
            show: auto
            step: 3
        }
    )
""")

    assert isinstance(a, Axis)
    assert a.minorTicks.show == 'auto'
    assert a.minorTicks.step == 3