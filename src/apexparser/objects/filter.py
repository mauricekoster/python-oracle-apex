from . import ApexGroup, ApexObject

class FilterLabel(ApexGroup):
    @property
    def label(self):
        return self.properties.get('label', None)
    

class FilterLov(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)
    
    

class FilterLayout(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    

class FilterSuggestions(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def staticValues(self):
        return self.properties.get('staticValues', None)
    
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)
    
    @property
    def showLabel(self):
        return self.properties.get('showLabel', None)


class FilterSource(ApexGroup):
    @property
    def databaseColumn(self):
        return self.properties.get('databaseColumn', None)
    
    @property
    def dbColumns(self):
        return self.properties.get('dbColumns', None)
    
    @property
    def dataType(self):
        return self.properties.get('dataType', None)
    

class Filter(ApexObject):
    # Properties
    @property
    def name(self):
        return self.properties.get('name', None)
    
    @property
    def type(self):
        return self.properties.get('type', None)
    
    # Groups

    @property
    def label(self) -> FilterLabel:
        return self.groups.get('label', None)
    
    @property
    def lov(self) -> FilterLov:
        return self.groups.get('lov', None)
    
    @property
    def layout(self) -> FilterLayout:
        return self.groups.get('layout', None)
    
    @property
    def suggestions(self) -> FilterSuggestions:
        return self.groups.get('suggestions', None)
    
    @property
    def source(self) -> FilterSource:
        return self.groups.get('source', None)
    
    