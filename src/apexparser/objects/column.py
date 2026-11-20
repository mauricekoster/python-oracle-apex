from . import ApexGroup, ApexObject


class ColumnHeading(ApexGroup):
    @property
    def heading(self):
        return self.properties.get('heading', None)

class ColumnLayout(ApexGroup):
    @property
    def sequence(self):
        return self.properties.get('sequence', None)
    @property
    def columnAlignment(self):
        return self.properties.get('columnAlignment', None)
    @property
    def group(self):
        return self.properties.get('group', None)


class ColumnAppearance(ApexGroup):
    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)

    @property
    def formatMask(self):
        return self.properties.get('formatMask', None)

    @property
    def backgroundColor(self):
        return self.properties.get('backgroundColor', None)

    @property
    def foregroundColor(self):
        return self.properties.get('foregroundColor', None)

    @property
    def barWidth(self):
        return self.properties.get('barWidth', None)

    @property
    def viewFileAs(self):
        return self.properties.get('viewFileAs', None)

    @property
    def downloadText(self):
        return self.properties.get('downloadText', None)

    @property
    def group(self):
        return self.properties.get('group', None)


class ColumnSource(ApexGroup):
    @property
    def type(self):
        return self.properties.get('type', None)
    
    @property
    def databaseColumn(self):
        return self.properties.get('databaseColumn', None)
    
    @property
    def sqlExpression(self):
        return self.properties.get('sqlExpression', None)
    
    @property
    def primaryKey(self):
        return self.properties.get('primaryKey', None)

    @property
    def dataType(self):
        return self.properties.get('dataType', None)

    @property
    def availableOnClient(self):
        return self.properties.get('availableOnClient', None)

    @property
    def valueProtected(self):
        return self.properties.get('valueProtected', None)

    @property
    def timezoneAware(self):
        return self.properties.get('timezoneAware', None)


class Column(ApexObject):
    @property
    def columnName(self):
        return self.properties.get('columnName', None)

    @property
    def name(self):
        return self.properties.get('name', None)

    @property
    def type(self):
        return self.properties.get('type', None)

    @property
    def heading(self) -> ColumnHeading:
        return self.groups.get('heading', ColumnHeading())

    @property
    def layout(self) -> ColumnLayout:
        return self.groups.get('layout', ColumnLayout())

    @property
    def appearance(self) -> ColumnAppearance:
        return self.groups.get('appearance', ColumnAppearance())

    @property
    def source(self) -> ColumnSource:
        return self.groups.get('source', ColumnSource())