from . import ApexGroup, ApexObject


class SortSort(ApexGroup):
    @property
    def direction(self):
        return self.properties.get('direction', None)
    
    @property
    def nulls(self):
        return self.properties.get('nulls', None)
    
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    
    


class Sort(ApexObject):

    # Properties

    @property
    def column(self):
        return self.properties.get('column', None)

    # Groups
    
    @property
    def sort(self) -> SortSort:
        return self.groups.get('sort', None)
    
    