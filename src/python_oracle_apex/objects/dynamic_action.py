from . import ApexGroup, ApexObject


class DynamicActionExecution(ApexGroup):
    pass

class DynamicActionWhen(ApexGroup):
    pass

class DynamicActionClientSideCondition(ApexGroup):
    pass

class DynamicAction(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

