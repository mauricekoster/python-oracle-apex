from apexparser import *


def test_series_0(apex_parser):
    s = apex_parser.parse(
"""series A (
    )
""")

    assert isinstance(s, Series)

def test_series_properties(apex_parser):
    s = apex_parser.parse(
"""series A (
        name: Sales Over Time
        type: area
    )
""")

    assert isinstance(s, Series)
    assert s.name == 'Sales Over Time'
    assert s.type == 'area'


def test_series_execution(apex_parser):
    s = apex_parser.parse(
"""series A (
        name: Sales Over Time
        execution {
            sequence: 10
        }
    )
""")

    assert isinstance(s, Series)
    assert s.name == 'Sales Over Time'
    assert s.execution.sequence == 10
  

def test_series_source(apex_parser):
    s = apex_parser.parse(
"""series A (
        name: Sales Over Time
        source {
            location: regionSource
        }
    )
""")

# TODO: source
# remoteServer
# sampleData
# type
# tableOwner
# tableName
# includeRowidColumn
# whereClause
# graphOwner
# graphName
# matchClause
# columnsClause
# sqlQuery
# language
# plsqlFunctionBody
# javaScriptFunctionBody
# restSource
# jsonDualityView
# jsonSource
# pageItemsToSubmit
# optimizerHint

    assert isinstance(s, Series)
    assert s.name == 'Sales Over Time'
    assert s.source.location == 'regionSource'


def test_series_column_mapping(apex_parser):
    s = apex_parser.parse(
"""series A (
        name: Sales Over Time
        columnMapping {
            label: SALE_DATE
            value: TOTAL_SALES
        }
    )
""")

# TODO: columnMapping
# seriesName
# valueAggregation
# open
# low
# high
# close
# volume
# x
# y
# z
# targetValue
# minValue
# maxValue
# rowId
# rowName
# taskId
# taskName
# taskStartDate
# taskEndDate
# progress
# baselineStartDate
# baselineEndDate
# customTooltip
# legendTooltip
# labelTooltip
# customColumn

    assert isinstance(s, Series)
    assert s.columnMapping.label == 'SALE_DATE'
    assert s.columnMapping.value == 'TOTAL_SALES'
