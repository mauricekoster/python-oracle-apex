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

    @property
    def tableName(self):
        return self.properties.get('tableName', None)
    
    @property
    def pkColumn(self):
        return self.properties.get('pkColumn', None)
    
    @property
    def pkItem(self):
        return self.properties.get('pkItem', None)


class ProcessTarget(ApexGroup):
    @property
    def tableName(self):
        return self.properties.get('tableName', None)
    
    @property
    def pkColumn(self):
        return self.properties.get('pkColumn', None)
    
    @property
    def pkItem(self):
        return self.properties.get('pkItem', None)
    
    @property
    def returnKeyIntoItem(self):
        return self.properties.get('returnKeyIntoItem', None)
    

class ProcessSuccessMessage(ApexGroup):
    @property
    def successMessage(self):
        return self.properties.get('successMessage', None)


class ProcessError(ApexGroup):
    @property
    def errorMessage(self):
        return self.properties.get('errorMessage', None)
    
    @property
    def displayLocation(self):
        return self.properties.get('displayLocation', None)


class ProcessServerSideCondition(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def value(self):
        return self.properties.get('value', None)

    @property
    def whenButtonPressed(self):
        return self.properties.get('whenButtonPressed', None)
    
    @property
    def item(self):
        return self.properties.get('item', None)
    
    

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

    @property
    def target(self) -> ProcessTarget:
        return self.groups.get('target', None)
    
    @property
    def successMessage(self) -> ProcessSuccessMessage:
        return self.groups.get('successMessage', None)
    
    @property
    def error(self) -> ProcessError:
        return self.groups.get('error', None)
    
    @property
    def serverSideCondition(self) -> ProcessServerSideCondition:
        return self.groups.get('serverSideCondition', None)
    