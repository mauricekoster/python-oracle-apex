from . import ApexGroup, ApexObject


class Aggregate(ApexObject):
    @property
    def function(self):
        return self.properties.get('function', None)
    
    @property
    def column(self):
        return self.properties.get('column', None)
    
    