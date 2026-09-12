from . import ApexGroup, ApexObject


class ComputationAExecution(ApexGroup):
    pass

class ComputationAComputation(ApexGroup):
    pass

class ComputationA(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)
