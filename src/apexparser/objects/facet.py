from . import ApexGroup, ApexObject


class FacetLabel(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def label(self):
        return self.properties.get('label', None)

    @property
    def showLabelForCurrentFacet(self):
        return self.properties.get('showLabelForCurrentFacet', None)

class FacetLov(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def type(self):
        return self.properties.get('type', None)


class FacetLayout(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def sequence(self):
        return self.properties.get('sequence', None)


class FacetListEntries(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def computeCounts(self):
        return self.properties.get('computeCounts', None)

    @property
    def maxDisplayedEntries(self):
        return self.properties.get('maxDisplayedEntries', None)


class FacetSource(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def databaseColumn(self):
        return self.properties.get('databaseColumn', None)

    
class Facet(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def label(self) -> FacetLabel:
        return self.groups.get('label', None)

    @property
    def lov(self) -> FacetLov:
        return self.groups.get('lov', None)

    @property
    def layout(self) -> FacetLayout:
        return self.groups.get('layout', None)

    @property
    def list_entries(self) -> FacetListEntries:
        return self.groups.get('list-entries', None)

    @property
    def source(self) -> FacetSource:
        return self.groups.get('source', None)