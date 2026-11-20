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
