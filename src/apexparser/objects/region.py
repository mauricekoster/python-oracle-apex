from . import ApexGroup, ApexObject, Column

class RegionLayout(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def parentRegion(self):
        return self.properties.get('parentRegion', None)


class RegionAppearance(ApexGroup):
    pass


class RegionSource(ApexGroup):
    @property
    def list(self):
        return self.properties.get('list', None)
    
    @property
    def breadcrumb(self):
        return self.properties.get('breadcrumb', None)
    
    @property
    def filteredRegion(self):
        return self.properties.get('filteredRegion', None)
    
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)
    
    @property
    def plsqlFunctionBody(self):
        return self.properties.get('plsqlFunctionBody', None)


class RegionAdvanced(ApexGroup):
    pass


class RegionComponentAppearance(ApexGroup):
    @property
    def display(self):
        return self.properties.get('display', None)
    @property
    def layout(self):
        return self.properties.get('layout', None)
    @property
    def gridColumns(self):
        return self.properties.get('gridColumns', None)
    @property
    def listTemplate(self):
        return self.properties.get('listTemplate', None)
    @property
    def breadcrumbTemplate(self):
        return self.properties.get('breadcrumbTemplate', None)
    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)
    @property
    def templateOptions(self):
        return self.properties.get('templateOptions', None)
    @property
    def templateType(self):
        return self.properties.get('templateType', None)
    @property
    def template(self):
        return self.properties.get('template', None)
    @property
    def customAttributes(self):
        return self.properties.get('customAttributes', None)
    @property
    def showNullValuesAs(self):
        return self.properties.get('showNullValuesAs', None)
    @property
    def selectFirstRow(self):
        return self.properties.get('selectFirstRow', None)
    @property
    def fixedRowHeight(self):
        return self.properties.get('fixedRowHeight', None)


class RegionImage(ApexGroup):
    pass


class RegionSettings(ApexGroup):
    pass


class RegionPluginAvatar(ApexGroup):
    @property
    def icon(self):
        return self.properties.get('icon', None)


class RegionPluginBadge(ApexGroup):
    @property
    def label(self):
        return self.properties.get('label', None)
    @property
    def value(self):
        return self.properties.get('value', None)


class RegionPagination(ApexGroup):
    @property
    def entitiesPerPage(self):
        return self.properties.get('entitiesPerPage', None)


class RegionAccessibility(ApexGroup):
    @property
    def useLandmark(self):
        return self.properties.get('useLandmark', None)
    @property
    def landmarkType(self):
        return self.properties.get('landmarkType', None)
    @property
    def landmarkLabel(self):
        return self.properties.get('landmarkLabel', None)


class RegionReportLayout(ApexGroup):
    @property
    def numberOfRowsType(self):
        return self.properties.get('numberOfRowsType', None)
    @property
    def numberOfRows(self):
        return self.properties.get('numberOfRows', None)
    @property
    def item(self):
        return self.properties.get('item', None)


class RegionPerformance(ApexGroup):
    @property
    def maxRowsToProcess(self):
        return self.properties.get('maxRowsToProcess', None)
    
    @property
    def lazyLoading(self):
        return self.properties.get('lazyLoading', None)


class RegionMessages(ApexGroup):
    @property
    def whenNoDataFound(self):
        return self.properties.get('whenNoDataFound', None)
    
    @property
    def whenMoreDataFound(self):
        return self.properties.get('whenMoreDataFound', None)
    
    @property
    def noDataFoundIcon(self):
        return self.properties.get('noDataFoundIcon', None)


class RegionComponentAdvanced(ApexGroup):
    @property
    def stripHtml(self):
        return self.properties.get('stripHtml', None)
    @property
    def sortNulls(self):
        return self.properties.get('sortNulls', None)
    @property
    def customSvgStyles(self):
        return self.properties.get('customSvgStyles', None)
    @property
    def oracleTextIndexColumn(self):
        return self.properties.get('oracleTextIndexColumn', None)
    @property
    def emailFromAddress(self):
        return self.properties.get('emailFromAddress', None)
    @property
    def initJavaScriptFunction(self):
        return self.properties.get('initJavaScriptFunction', None)
    @property
    def regionAlias(self):
        return self.properties.get('regionAlias', None)
    @property
    def reportIdItem(self):
        return self.properties.get('reportIdItem', None)
    @property
    def maxRowsPerPageInSelector(self):
        return self.properties.get('maxRowsPerPageInSelector', None)


class Region(ApexObject):
    # direct

    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def title(self):
        return self.properties.get('title', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    # group

    @property
    def layout(self) -> RegionLayout:
        return self.groups.get('layout', None)

    @property
    def appearance(self) -> RegionAppearance:
        return self.groups.get('appearance', None)

    @property
    def settings(self) -> RegionSettings:
        return self.groups.get('settings', None)

    @property
    def plugin_avatar(self) -> RegionPluginAvatar:
        return self.groups.get('plugin-avatar', None)

    @property
    def plugin_badge(self) -> RegionPluginBadge:
        return self.groups.get('plugin-badge', None)

    @property
    def source(self) -> RegionSource:
        return self.groups.get('source', None)

    @property
    def pagination(self) -> RegionPagination:
        return self.groups.get('pagination', None)

    @property
    def accessibility(self) -> RegionAccessibility:
        return self.groups.get('accessibility', None)

    @property
    def reportLayout(self) -> RegionReportLayout:
        return self.groups.get('reportLayout', None)

    @property
    def performance(self) -> RegionPerformance:
        return self.groups.get('performance', None)

    @property
    def messages(self) -> RegionMessages:
        return self.groups.get('messages', None)

    @property
    def componentAppearance(self) -> RegionComponentAppearance:
        return self.groups.get('componentAppearance', None)

    @property
    def componentAdvanced(self) -> RegionComponentAdvanced:
        return self.groups.get('componentAdvanced', None)

    # child

    @property
    def columns(self) -> list[Column]:
        return [x for x in self.children if isinstance(x, Column)]
    