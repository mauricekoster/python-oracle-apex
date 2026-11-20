from . import ApexGroup, ApexObject


class ActionAffectedElements(ApexGroup):
    pass

class ActionExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def fireOnInit(self):
        return self.properties.get('fireOnInit', None)



class ActionLayout(ApexGroup):
    @property
    def position(self):
        return self.properties.get('position', None)

    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    
class ActionAppearance(ApexGroup):
    @property
    def icon(self):
        return self.properties.get('icon', None)

    @property
    def hot(self):
        return self.properties.get('hot', None)

    @property
    def displayType(self):
        return self.properties.get('displayType', None)

    @property
    def showAsDisabled(self):
        return self.properties.get('showAsDisabled', None)

    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)

    
class ActionBehavior(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def target(self) -> dict:
        return self.properties.get('target', None)

    @property
    def targetUrl(self):
        return self.properties.get('targetUrl', None)

    @property
    def linkAttributes(self):
        return self.properties.get('linkAttributes', None)
    

class Action(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)
    
    @property
    def action(self):
        return self.properties.get('action', None)
    
    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def position(self):
        return self.properties.get('position', None)

    @property
    def template(self):
        return self.properties.get('template', None)
    
    @property
    def label(self):
        return self.properties.get('label', None)

    @property
    def layout(self) -> ActionLayout:
        return self.groups.get('layout', ActionLayout())

    @property
    def appearance(self) -> ActionAppearance:
        return self.groups.get('appearance', ActionAppearance())    

    @property
    def behavior(self) -> ActionBehavior:
        return self.groups.get('behavior', ActionBehavior())    

    @property
    def execution(self) -> ActionExecution:
        return self.groups.get('execution', ActionExecution())    