from . import ApexGroup, ApexObject

class DisplayColumnIdentification(ApexGroup):
    @property
    def column(self):
        return self.properties.get('column', None)


class DisplayColumn(ApexObject):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    
    
    @property
    def identification(self) -> DisplayColumnIdentification:
        return self.groups.get('identification', None)
    
    