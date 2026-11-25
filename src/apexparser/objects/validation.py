from . import ApexGroup, ApexObject, Column


class ValidationValidation(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def plsqlFunctionBody(self):
        return self.properties.get('plsqlFunctionBody', None)
    
    

class ValidationExecution(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    
    
class ValidationError(ApexGroup):
    @property
    def errorMessage(self):
        return self.properties.get('errorMessage', None)
    
    @property
    def displayLocation(self):
        return self.properties.get('displayLocation', None)
    
    @property
    def associatedItem(self):
        return self.properties.get('associatedItem', None)
    
    @property
    def associatedColumn(self):
        return self.properties.get('associatedColumn', None)


class ValidationServerSideCondition(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def value(self):
        return self.properties.get('value', None)
    
    


class Validation(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)
    
    @property
    def execution(self) -> ValidationExecution:
        return self.groups.get('execution', None)
    
    @property
    def validation(self) -> ValidationValidation:
        return self.groups.get('validation', None)
    
    @property
    def error(self) -> ValidationError:
        return self.groups.get('error', None)
    
    @property
    def serverSideCondition(self) -> ValidationServerSideCondition:
        return self.groups.get('serverSideCondition', None)
    
        