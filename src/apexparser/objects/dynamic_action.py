from . import ApexGroup, ApexObject


class DynamicActionExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)


class DynamicActionWhen(ApexGroup):
    @property
    def selectionType(self):
        return self.properties.get('selectionType', None)
    
    @property
    def items(self):
        return self.properties.get('items', None)


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
