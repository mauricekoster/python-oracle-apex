from . import ApexGroup, ApexObject, Column

class Validation(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)
    
    