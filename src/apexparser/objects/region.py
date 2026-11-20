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
    pass


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

    # child

    @property
    def columns(self) -> list[Column]:
        return [x for x in self.children if isinstance(x, Column)]
    