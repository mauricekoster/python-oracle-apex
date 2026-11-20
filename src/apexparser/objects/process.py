from . import ApexGroup, ApexObject


class ProcessExecution(ApexGroup):
    @property
    def sequence(self):
        return self['sequence']

    @property
    def point(self):
        return self['point']

    @property
    def runProcess(self):
        return self['runProcess']


class ProcessAdvanced(ApexGroup):
    @property
    def staticId(self):
        return self['staticId']

    @property
    def executionMappingIdentifier(self):
        return self['executionMappingIdentifier']

class ProcessSource(ApexGroup):
    @property
    def location(self):
        return self['location']

    @property
    def language(self):
        return self['language']

    @property
    def remoteServer(self):
        return self['remoteServer']
    
    @property
    def plsqlCode(self):
        return self['plsqlCode']

class Process(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    @property
    def name(self):
        return self['name']

    @property
    def type(self):
        return self['type']

    @property
    def source(self) -> ProcessSource:
        return self['source']


    @property
    def execution(self):
        return self['execution']

    @property
    def advanced(self):
        return self['advanced']
