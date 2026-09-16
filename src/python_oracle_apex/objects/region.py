from . import ApexGroup, ApexObject

class RegionLayout(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def parentRegion(self):
        return self.properties.get('parentRegion', None)

class RegionAppearance(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)


class RegionSource(ApexGroup):
    pass


class RegionAdvanced(ApexGroup):
    pass


class RegionComponentAppearance(ApexGroup):
    pass


class RegionImage(ApexGroup):
    pass

class RegionSettings(ApexGroup):
    pass


class Region(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def title(self):
        return self.properties.get('title', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def layout(self):
        return self.groups.get('layout', RegionLayout())

    @property
    def appearance(self):
        return self.groups.get('appearance', RegionAppearance())
  