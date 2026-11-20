from apexparser import *


def test_region_0(apex_parser):
    r = apex_parser.parse(
"""region A (
    )
""")

    assert isinstance(r, Region)


def test_region_source(apex_parser):
    r = apex_parser.parse(
"""region A (
        source {
            list: @application-actions
            plsqlFunctionBody:
                ```plsql
                declare
                begin
                end;
                ```
        }
    )
""")

# TODO:
# "sqlQuery"
# "plsqlCode"
# "htmlCode"
# "text"
# "language"
# "javaScriptFunctionBody"
# "location"
# "remoteServer"
# "sampleData"
# "type"
# "tableOwner"
# "tableName"
# "includeRowidColumn"
# "whereClause"
# "graphOwner"
# "graphName"
# "matchClause"
# "columnsClause"
# "orderByClause"
# "restSource"
# "jsonDualityView"
# "jsonSource"
# "breadcrumb"
# "filteredRegion"
# "pageItemsToSubmit"
# "optimizerHint"
# "useGenericColumnNames"
# "genericColumnCount"



    assert isinstance(r, Region)

    assert r.source.list == '@application-actions'
    assert r.source.plsqlFunctionBody == '```plsql\ndeclare\nbegin\nend;\n```'


def test_region_plugin_avatar(apex_parser):
    r = apex_parser.parse(
"""region A (
        plugin-avatar {
            icon: fa-tag
        }
    )
""")

    assert isinstance(r, Region)

    assert r.plugin_avatar.icon == 'fa-tag'

def test_region_plugin_badge(apex_parser):
    r = apex_parser.parse(
"""region A (
        plugin-badge {
            label: Sale
            value: SALE
        }
    )
""")

    assert isinstance(r, Region)

    assert r.plugin_badge.label == 'Sale'
    assert r.plugin_badge.value == 'SALE'

def test_region_pagination(apex_parser):
    r = apex_parser.parse(
"""region A (
        pagination {
            entitiesPerPage: 100
        }
    )
""")

    assert isinstance(r, Region)

    assert r.pagination.entitiesPerPage == 100


def test_region_accessibility(apex_parser):
    r = apex_parser.parse(
"""region A (
        accessibility {
            useLandmark: true
            landmarkType: region
            landmarkLabel: Applepie
        }
    )
""")

    assert isinstance(r, Region)

    assert r.accessibility.useLandmark == True

def test_region_report_layout(apex_parser):
    r = apex_parser.parse(
"""region A (
        reportLayout {
            numberOfRowsType: staticValue
            numberOfRows: 1000
            item: something
        }
    )
""")

    assert isinstance(r, Region)

    assert r.reportLayout.numberOfRowsType == "staticValue"
    assert r.reportLayout.numberOfRows == 1000
    assert r.reportLayout.item == "something"


def test_region_performance(apex_parser):
    r = apex_parser.parse(
"""region A (
        performance {
            lazyLoading: false
            maxRowsToProcess: 1000
        }
    )
""")

    assert isinstance(r, Region)

    assert r.performance.maxRowsToProcess == 1000
    assert r.performance.lazyLoading == False


def test_region_messages(apex_parser):
    r = apex_parser.parse(
"""region A (
        messages {
            whenNoDataFound: no data found
            whenMoreDataFound: more data found
            noDataFoundIcon: icon-name
        }
    )
""")

    assert isinstance(r, Region)

    assert r.messages.whenNoDataFound == 'no data found'
    assert r.messages.whenMoreDataFound == 'more data found'
    assert r.messages.noDataFoundIcon == 'icon-name'
