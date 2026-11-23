from . import ApexGroup, ApexObject

class AxisValue(ApexGroup):
    @property
    def min(self):
        return self.properties.get('min', None)
    
    @property
    def max(self):
        return self.properties.get('max', None)
    
    @property
    def format(self):
        return self.properties.get('format', None)
    
    @property
    def decimalPlaces(self):
        return self.properties.get('decimalPlaces', None)
    
    @property
    def currency(self):
        return self.properties.get('currency', None)
    
    @property
    def pattern(self):
        return self.properties.get('pattern', None)
    
    @property
    def formatScaling(self):
        return self.properties.get('formatScaling', None)
    
    @property
    def baselineScaling(self):
        return self.properties.get('baselineScaling', None)
    
    @property
    def scale(self):
        return self.properties.get('scale', None)
    
    @property
    def step(self):
        return self.properties.get('step', None)
    

class AxisMinorTicks(ApexGroup):
    @property
    def show(self):
        return self.properties.get('show', None)
    
    @property
    def step(self):
        return self.properties.get('step', None)
    
    


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
    
    
    @property
    def value(self) -> AxisValue:
        return self.groups.get('value', None)
    
    @property
    def minorTicks(self) -> AxisMinorTicks:
        return self.groups.get('minorTicks', None)
    
    