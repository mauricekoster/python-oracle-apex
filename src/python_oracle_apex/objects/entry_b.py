from . import ApexGroup, ApexObject


class EntryBExecution(ApexGroup):
    pass

class EntryBLink(ApexGroup):
    pass

class EntryB(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', "<NONAME>")
    
    @property
    def pageNumber(self):
        return self.properties.get('pageNumber', None)

