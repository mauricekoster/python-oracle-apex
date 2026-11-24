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


class PageItemDefault(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def staticValue(self):
        return self.properties.get('staticValue', None)



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
    
    