from . import ApexGroup, ApexObject


class PageItemLabel(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def label(self):
        return self.properties.get('label', None) 
    
    @property
    def alignment(self):
        return self.properties.get('alignment', None) 

class PageItemSettings(ApexGroup):
    @property
    def trimSpaces(self):
        return self.properties.get('trimSpaces', None)
    
    @property
    def showControls(self):
        return self.properties.get('showControls', None)

    @property
    def valueProtected(self):
        return self.properties.get('valueProtected', None)
    
    @property
    def minValue(self):
        return self.properties.get('minValue', None)
    
    @property
    def maxValue(self):
        return self.properties.get('maxValue', None)
    
    @property
    def numberAlignment(self):
        return self.properties.get('numberAlignment', None)
    
    @property
    def virtualKeyboard(self):
        return self.properties.get('virtualKeyboard', None)
    
    
    
class PageItemLayout(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def region(self):
        return self.properties.get('region', None)

    @property
    def slot(self):
        return self.properties.get('slot', None)

    @property
    def startNewRow(self):
        return self.properties.get('startNewRow', None)
    
    

class PageItemSource(ApexGroup):    
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def databaseColumn(self):
        return self.properties.get('databaseColumn', None)
    
    @property
    def used(self):
        return self.properties.get('used', None)
    
    @property
    def plsqlFunctionBody(self):
        return self.properties.get('plsqlFunctionBody', None)
    
    


class PageItemAppearance(ApexGroup):
    @property
    def template(self):
        return self.properties.get('template', None)

    @property
    def templateOptions(self):
        return self.properties.get('templateOptions', None)

    @property
    def height(self):
        return self.properties.get('height', None)

    @property
    def formatMask(self):
        return self.properties.get('formatMask', None)
    
    @property
    def width(self):
        return self.properties.get('width', None)
    

class PageItemValidation(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)


class PageItemAdvanced(ApexGroup):
    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)
    

class PageItemSessionState(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)

class PageItemSecurity(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)

class PageItemLov(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def lov(self):
        return self.properties.get('lov', None)

    @property
    def displayNullValue(self):
        return self.properties.get('displayNullValue', None)

    @property
    def nullDisplayValue(self):
        return self.properties.get('nullDisplayValue', None)
    
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)
    
    

class PageItemDefault(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def staticValue(self):
        return self.properties.get('staticValue', None)
    
    @property
    def sqlQuerySingleValue(self):
        return self.properties.get('sqlQuerySingleValue', None)
    

class PageItemServerSideCondition(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)


class PageItem(ApexObject):

    @property
    def name(self):
        return self.properties.get('name', self.component_id)

    @property
    def type(self):
        return self.properties.get('type', None)


    @property
    def layout(self) -> PageItemLayout:
        return self.groups.get('layout', PageItemLayout())

    @property
    def label(self) -> PageItemLabel:
        return self.groups.get('label', PageItemLabel())

    @property
    def lov(self) -> PageItemLov:
        return self.groups.get('lov', PageItemLov())

    @property
    def appearance(self) -> PageItemAppearance:
        return self.groups.get('appearance', PageItemAppearance())
    
    @property
    def default(self) -> PageItemDefault:
        return self.groups.get('default', PageItemDefault())

    @property
    def source(self) -> PageItemSource:
        return self.groups.get('source', None)
    
    @property
    def advanced(self) -> PageItemAdvanced:
        return self.groups.get('advanced', None)
    
    @property
    def settings(self) -> PageItemSettings:
        return self.groups.get('settings', None)

    @property
    def serverSideCondition(self) -> PageItemServerSideCondition:
        return self.groups.get('serverSideCondition', None)
    
    
    