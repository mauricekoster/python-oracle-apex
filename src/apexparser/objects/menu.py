from . import ApexGroup, ApexObject

class MenuLayout(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    

class MenuBehavior(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def target(self):
        return self.properties.get('target', None)
    
    @property
    def targetUrl(self):
        return self.properties.get('targetUrl', None)
    
    @property
    def linkAttributes(self):
        return self.properties.get('linkAttributes', None)
    
    

class Menu(ApexObject):
    # Properties
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def label(self):
        return self.properties.get('label', None)
    
    @property
    def parentMenu(self):
        return self.properties.get('parentMenu', None)
    
    
    # Groups
    @property
    def layout(self) -> MenuLayout:
        return self.groups.get('layout', None)
    
    @property
    def behavior(self) -> MenuBehavior:
        return self.groups.get('behavior', None)
    
    
    # Children