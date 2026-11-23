from . import ApexGroup, ApexObject


class DynamicActionExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)


class DynamicActionWhen(ApexGroup):
    @property
    def event(self):
        return self.properties.get('event', None)
    
    @property
    def customEvent(self):
        return self.properties.get('customEvent', None)
        
    @property
    def selectionType(self):
        return self.properties.get('selectionType', None)

    @property
    def region(self):
        return self.properties.get('region', None)
    
    @property
    def interactiveGrid(self):
        return self.properties.get('interactiveGrid', None)
    
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
    
    

class DynamicActionClientSideCondition(ApexGroup):
    pass


class DynamicAction(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def execution(self) -> DynamicActionExecution:
        return self.groups.get('execution', DynamicActionExecution())

    @property
    def when(self) -> DynamicActionWhen:
        return self.groups.get('when', DynamicActionWhen())
