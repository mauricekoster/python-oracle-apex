from . import ApexGroup, ApexObject


class Axis(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def showAxis(self):
        return self.properties.get('showAxis', None)
    
    @property
    def title(self):
        return self.properties.get('title', None)
    
    
    