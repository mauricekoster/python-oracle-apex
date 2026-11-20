from . import ApexGroup, ApexObject

class BranchExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)


class BranchBehavior(ApexGroup):
    @property
    def target(self):
        return self.properties.get('target', None)


class Branch(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def behavior(self) -> BranchBehavior:
        return self.groups.get('behavior', None)

    @property
    def execution(self) -> BranchExecution:
        return self.groups.get('execution', None)