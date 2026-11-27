from . import ApexGroup, ApexObject


class SavedReportDescription(ApexGroup):
    @property
    def description(self):
        return self.properties.get('description', None)
    
class SavedReportView(ApexGroup):
    @property
    def chart(self):
        return self.properties.get('chart', None)
    
    @property
    def groupBy(self):
        return self.properties.get('groupBy', None)
    
    @property
    def pivot(self):
        return self.properties.get('pivot', None)
    
    @property
    def default(self):
        return self.properties.get('default', None)

    @property
    def rowsPerPage(self):
        return self.properties.get('rowsPerPage', None)
    

class SavedReport(ApexObject):

    # Properties

    @property
    def name(self):
        return self.properties.get('name', None)
    
    @property
    def visibility(self):
        return self.properties.get('visibility', None)
    
    @property
    def staticId(self):
        return self.properties.get('staticId', None)
    
    # Groups   
        
    @property
    def description(self) -> SavedReportDescription:
        return self.groups.get('description', None)
    
    
    @property
    def view(self) -> SavedReportView:
        return self.groups.get('view', None)
    
    