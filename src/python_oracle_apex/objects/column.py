from . import ApexGroup, ApexObject


class ColumnHeading(ApexGroup):
    @property
    def heading(self):
        return self.properties.get('heading', None)

class Column(ApexObject):
    @property
    def columnName(self):
        return self.properties.get('columnName', None)

    # @property
    # def name(self):
    #     return self.properties.get('name', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def heading(self) -> ColumnHeading:
        return self.groups.get('heading', ColumnHeading())