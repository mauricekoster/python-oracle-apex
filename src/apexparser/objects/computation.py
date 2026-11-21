from . import ApexGroup, ApexObject


class ComputationExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    @property
    def point(self):
        return self.properties.get('point', None)


class ComputationComputation(ApexGroup):
    @property
    def sqlQuery(self):
        return self.properties.get('sqlQuery', None)


class Computation(ApexObject):
    # Properties
    
    @property
    def itemName(self):
        return self.properties.get('itemName', None)

    # Groups
    
    @property
    def execution(self) -> ComputationExecution:
        return self.groups.get('execution', None)

    @property
    def computation(self) -> ComputationComputation:
        return self.groups.get('computation', None)