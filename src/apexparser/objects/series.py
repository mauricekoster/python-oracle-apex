from . import ApexGroup, ApexObject

class SeriesExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    

class SeriesSource(ApexGroup):
    @property
    def location(self):
        return self.properties.get('location', None)
    
    

class SeriesColumnMapping(ApexGroup):
    @property
    def label(self):
        return self.properties.get('label', None)
    
    @property
    def value(self):
        return self.properties.get('value', None)
    

class SeriesLine(ApexGroup):
    pass

class Series(ApexObject):

    # Properties

    @property
    def name(self):
        return self.properties.get('name', None)
    
    @property
    def type(self):
        return self.properties.get('type', None)
    
    # Groups

    @property
    def execution(self) -> SeriesExecution:
        return self.groups.get('execution', None)

    @property
    def source(self) -> SeriesSource:
        return self.groups.get('source', None)
    
    @property
    def line(self) -> SeriesLine:
        return self.groups.get('line', None)
    
    @property
    def columnMapping(self) -> SeriesColumnMapping:
        return self.groups.get('columnMapping', None)
    
    