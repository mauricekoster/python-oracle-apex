from . import ApexGroup, ApexObject


class ActionAffectedElements(ApexGroup):
    @property
    def selectionType(self):
        return self.properties.get('selectionType', None)
    @property
    def region(self):
        return self.properties.get('region', None)
    @property
    def columns(self):
        return self.properties.get('columns', None)
    @property
    def button(self):
        return self.properties.get('button', None)
    @property
    def items(self):
        return self.properties.get('items', None)
    @property
    def domObject(self):
        return self.properties.get('domObject', None)
    @property
    def jquerySelector(self):
        return self.properties.get('jquerySelector', None)
    @property
    def javaScriptExpression(self):
        return self.properties.get('javaScriptExpression', None)
    

class ActionExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    @property
    def fireWhenEventResultIs(self):
        return self.properties.get('fireWhenEventResultIs', None)
    @property
    def fireOnInit(self):
        return self.properties.get('fireOnInit', None)
    @property
    def stopExecutionOnError(self):
        return self.properties.get('stopExecutionOnError', None)
    @property
    def waitForResult(self):
        return self.properties.get('waitForResult', None)


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
    

class ActionSettings(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)
    @property
    def itemsToSubmit(self):
        return self.properties.get('itemsToSubmit', None)
    @property
    def plsqlCode(self):
        return self.properties.get('plsqlCode', None)
    
    

class Action(ApexObject):

    # Properties

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

    # Groups

    @property
    def layout(self) -> ActionLayout:
        return self.groups.get('layout', None)
    @property
    def appearance(self) -> ActionAppearance:
        return self.groups.get('appearance', None)    
    @property
    def behavior(self) -> ActionBehavior:
        return self.groups.get('behavior', None)    
    @property
    def execution(self) -> ActionExecution:
        return self.groups.get('execution', None)    
    @property
    def affectedElements(self) -> ActionAffectedElements:
        return self.groups.get('affectedElements', None)    
    @property
    def settings(self) -> ActionSettings:
        return self.groups.get('settings', None)    