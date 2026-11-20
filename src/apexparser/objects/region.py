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
        return self.groups.get('layout', RegionLayout())

    @property
    def appearance(self) -> RegionAppearance:
        return self.groups.get('appearance', RegionAppearance())

    @property
    def settings(self) -> RegionSettings:
        return self.groups.get('settings', RegionSettings())

    @property
    def plugin_avatar(self) -> RegionPluginAvatar:
        return self.groups.get('plugin-avatar', RegionPluginAvatar())

    @property
    def plugin_badge(self) -> RegionPluginBadge:
        return self.groups.get('plugin-badge', RegionPluginBadge())

    @property
    def source(self) -> RegionSource:
        return self.groups.get('source', RegionSource())

    @property
    def pagination(self) -> RegionPagination:
        return self.groups.get('pagination', RegionPagination())

    @property
    def accessibility(self) -> RegionAccessibility:
        return self.groups.get('accessibility', RegionAccessibility())

    # child

    @property
    def columns(self) -> list[Column]:
        return [x for x in self.children if isinstance(x, Column)]
    