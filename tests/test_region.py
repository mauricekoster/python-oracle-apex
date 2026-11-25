from apexparser import *


def test_region_0(apex_parser):
    r = apex_parser.parse(
"""region A (
    )
""")

    assert isinstance(r, Region)


def test_region_1(apex_parser):
    r = apex_parser.parse(
"""region (
    )
""")

    assert isinstance(r, Region)


def test_region_settings(apex_parser):
    r = apex_parser.parse(
"""region A (
        settings {
            timeAxisType: mixedFrequency
            zoomAndScroll: liveScrollOnly
            overline: &REGION.
        }
    )
""")

# TODO: settings
# zoomDirection
# initialZooming
# showHorizontalGrid
# showVerticalGrid
# showRowAxis
# axisPosition
# pieSelectionEffect
# renderAs
# compactNosThreshold
# showCurrentFacets
# currentFacetsSelector
# displayChartForTopNValues
# title
# description
# miscellaneous
# displayAvatar
# displayBadge

    assert isinstance(r, Region)
    r.settings.timeAxisType == 'mixedFrequency'
    r.settings.zoomAndScroll == 'liveScrollOnly'
    r.settings.overline == '&REGION.'

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
            state: STATUS_COLOR
            columnWidth: small
        }
    )
""")

    assert isinstance(r, Region)

    assert r.plugin_badge.label == 'Sale'
    assert r.plugin_badge.value == 'SALE'
    assert r.plugin_badge.state == 'STATUS_COLOR'
    assert r.plugin_badge.columnWidth == 'small'

def test_region_pagination(apex_parser):
    r = apex_parser.parse(
"""region A (
        pagination {
            type: something
            displayPosition: bottomLeft
            partialPageRefresh: true
            showTotalCount: false
            maxRowsToDisplay: all
            cardsPerPage: 10
            entitiesPerPage: 100
            initialEntitiesCount: 10
        }
    )
""")

    assert isinstance(r, Region)

    assert r.pagination.type == 'something'
    assert r.pagination.displayPosition == 'bottomLeft'
    assert r.pagination.partialPageRefresh == True
    assert r.pagination.showTotalCount == False
    assert r.pagination.maxRowsToDisplay == 'all'
    assert r.pagination.cardsPerPage == 10
    assert r.pagination.entitiesPerPage == 100
    assert r.pagination.initialEntitiesCount == 10


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



def test_region_component_appearance(apex_parser):
    r = apex_parser.parse(
"""region A (
        componentAppearance {
            display: text
            layout: float
            gridColumns: 5
            listTemplate: @/test
            breadcrumbTemplate: @/breadcrumb
            cssClasses: warning
            templateOptions: #DEFAULT#
            templateType: theme
            template: @/test
            customAttributes: mummy
            showNullValuesAs: NIX
            selectFirstRow: true
            fixedRowHeight: false
        }
    )
""")

    assert isinstance(r, Region)

    assert r.componentAppearance.display == 'text'
    assert r.componentAppearance.layout == 'float'
    assert r.componentAppearance.gridColumns == '5'
    assert r.componentAppearance.listTemplate == '@/test'
    assert r.componentAppearance.breadcrumbTemplate == '@/breadcrumb'
    assert r.componentAppearance.cssClasses == ['warning']
    assert r.componentAppearance.templateOptions == ['#DEFAULT#']
    assert r.componentAppearance.templateType == 'theme'
    assert r.componentAppearance.template == '@/test'
    assert r.componentAppearance.customAttributes == 'mummy'
    assert r.componentAppearance.showNullValuesAs == 'NIX'
    assert r.componentAppearance.selectFirstRow == True
    assert r.componentAppearance.fixedRowHeight == False


def test_region_component_advanced(apex_parser):
    r = apex_parser.parse(
"""region A (
        componentAdvanced {
            stripHtml: true
            sortNulls: first
            customSvgStyles:
                ```css
                .a { text-color: red; }
                ```
            oracleTextIndexColumn: something
            emailFromAddress: admin@example.com
            initJavaScriptFunction:
                ```javascript
                ```
            regionAlias: alias
            reportIdItem: id
            maxRowsPerPageInSelector: yes
        }
    )
""")

    assert isinstance(r, Region)

    assert r.componentAdvanced.stripHtml == True
    assert r.componentAdvanced.sortNulls == 'first'
    assert r.componentAdvanced.customSvgStyles == "```css\n.a { text-color: red; }\n```"
    assert r.componentAdvanced.oracleTextIndexColumn == 'something'
    assert r.componentAdvanced.emailFromAddress == 'admin@example.com'
    assert r.componentAdvanced.initJavaScriptFunction == '```javascript\n```'
    assert r.componentAdvanced.regionAlias == 'alias'
    assert r.componentAdvanced.reportIdItem == 'id'
    assert r.componentAdvanced.maxRowsPerPageInSelector == 'yes'


def test_region_chart(apex_parser):
    r = apex_parser.parse(
"""region A (
        chart {
            type: lineWithArea
        }
    )
""")

    assert isinstance(r, Region)

    assert r.chart.type == 'lineWithArea'


def test_region_chart_layout(apex_parser):
    r = apex_parser.parse(
"""region A (
        chartLayout {
            maxWidth: 800
            height: 480
        }
    )
""")

    assert isinstance(r, Region)

    assert r.chartLayout.maxWidth == 800
    assert r.chartLayout.height == 480


def test_region_title(apex_parser):
    r = apex_parser.parse(
"""region A (
        title {
            title: Test
            advancedFormatting: true
            column: AAA
            htmlExpression:
                ```html
                ```
            cssClasses: [
                red
                green
                blue
            ]
        }
    )
""")

    assert isinstance(r, Region)

    assert r.title.title == 'Test'
    assert r.title.advancedFormatting == True
    assert r.title.column == 'AAA'
    assert r.title.htmlExpression == '```html\n```'
    assert r.title.cssClasses == ['red', 'green', 'blue']


def test_region_legend(apex_parser):
    r = apex_parser.parse(
"""region A (
        legend {
            show: false
            title: Title
            position: start
            selector: sel
            cssClasses: elegant
            hideAndShowBehavior: none
            fontFamily: times
            fontStyle: normal
            fontSize: 22
            fontColor: blue
        }
    )
""")

    assert isinstance(r, Region)

    assert r.legend.show == False
    assert r.legend.title == 'Title'
    assert r.legend.position == 'start'
    assert r.legend.selector == 'sel'
    assert r.legend.cssClasses == ['elegant']
    assert r.legend.hideAndShowBehavior == 'none'
    assert r.legend.fontFamily == 'times'
    assert r.legend.fontStyle == 'normal'
    assert r.legend.fontSize == '22'
    assert r.legend.fontColor == 'blue'


def test_region_server_side_condition(apex_parser):
    r = apex_parser.parse(
"""region A (
        serverSideCondition {
            type: expression
            language: sql
            sqlExpression: 1=1
        }
    )
""")

# TODO: serverSideCondition
# missing

    assert isinstance(r, Region)
    assert r.serverSideCondition.type == 'expression'
    assert r.serverSideCondition.language == 'sql'
    assert r.serverSideCondition.sqlExpression == '1=1'


def test_region_entity_title(apex_parser):
    r = apex_parser.parse(
"""region A (
        entityTitle {
            singular: Store
            plural: Stores
        }
    )
""")

    assert isinstance(r, Region)
    assert r.entityTitle.singular == 'Store'
    assert r.entityTitle.plural == 'Stores'


def test_region_gen_ai(apex_parser):
    r = apex_parser.parse(
"""region A (
        genAI {
            naturalLanguageSupport: true
        }
    )
""")

# TODO: genAI

    assert isinstance(r, Region)
    assert r.genAI.naturalLanguageSupport == True

