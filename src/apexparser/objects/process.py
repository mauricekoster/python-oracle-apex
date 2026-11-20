from . import ApexGroup, ApexObject


class ProcessExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def point(self):
        return self.properties.get('point', None)

    @property
    def runProcess(self):
        return self.properties.get('runProcess', None)


class ProcessAdvanced(ApexGroup):
    @property
    def staticId(self):
        return self.properties.get('staticId', None)

    @property
    def executionMappingIdentifier(self):
        return self.properties.get('executionMappingIdentifier', None)


class ProcessSource(ApexGroup):
    @property
    def location(self):
        return self.properties.get('location', None)

    @property
    def language(self):
        return self.properties.get('language', None)

    @property
    def remoteServer(self):
        return self.properties.get('remoteServer', None)
    
    @property
    def plsqlCode(self):
        return self.properties.get('plsqlCode', None)


class Process(ApexObject):
    # Properties
    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    # Groups
    @property
    def source(self) -> ProcessSource:
        return self.groups.get('source', None)

    @property
    def execution(self) -> ProcessExecution:
        return self.groups.get('execution', None)

    @property
    def advanced(self) -> ProcessAdvanced:
        return self.groups.get('advanced', None)
