from . import ApexGroup, ApexObject


class AggregateAdvanced(ApexGroup):
    @property
    def staticId(self):
        return self.properties.get('staticId', None)
    
    @property
    def enabled(self):
        return self.properties.get('enabled', None)
    

class Aggregate(ApexObject):
    @property
    def function(self):
        return self.properties.get('function', None)
    
    @property
    def column(self):
        return self.properties.get('column', None)
    
    @property
    def function(self):
        return self.properties.get('function', None)
    
    @property
    def showGrandTotal(self):
        return self.properties.get('showGrandTotal', None)
    
    @property
    def tooltip(self):
        return self.properties.get('tooltip', None)
    
    # Groups
    @property
    def advanced(self) -> AggregateAdvanced:
        return self.groups.get('advanced', None)
    
    