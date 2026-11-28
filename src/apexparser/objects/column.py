from . import ApexGroup, ApexObject


class ColumnHeading(ApexGroup):
    @property
    def heading(self):
        return self.properties.get('heading', None)
    
    @property
    def alignment(self):
        return self.properties.get('alignment', None)

    @property
    def alternativeLabel(self):
        return self.properties.get('alternativeLabel', None)


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
    def width(self):
        return self.properties.get('width', None)

    @property
    def height(self):
        return self.properties.get('height', None)

    @property
    def template(self):
        return self.properties.get('template', None)

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


class ColumnSorting(ApexGroup):
    @property
    def defaultSequence(self):
        return self.properties.get('defaultSequence', None)
    @property
    def direction(self):
        return self.properties.get('direction', None)
    @property
    def sortable(self):
        return self.properties.get('sortable', None)


class ColumnLink(ApexGroup):
    @property
    def target(self):
        return self.properties.get('target', None)
    @property
    def linkText(self):
        return self.properties.get('linkText', None)
    @property
    def linkAttributes(self):
        return self.properties.get('linkAttributes', None)


class ColumnAdvanced(ApexGroup):
    @property
    def htmlDomId(self):
        return self.properties.get('htmlDomId', None)
    
    @property
    def endUserAlias(self):
        return self.properties.get('endUserAlias', None)

    @property
    def computeSum(self):
        return self.properties.get('computeSum', None)
    
    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)
    
    @property
    def customAttributes(self):
        return self.properties.get('customAttributes', None)
    
    @property
    def cellWidth(self):
        return self.properties.get('cellWidth', None)
    

class ColumnExportPrinting(ApexGroup):
    @property
    def includeInExportPrint(self):
        return self.properties.get('includeInExportPrint', None)
    
    @property
    def printWidth(self):
        return self.properties.get('printWidth', None)


class ColumnColumnFilter(ApexGroup):
    @property
    def lovType(self):
        return self.properties.get('lovType', None)
    
    

    
class ColumnLink(ApexGroup):
    @property
    def target(self):
        return self.properties.get('target', None)
    
    @property
    def linkText(self):
        return self.properties.get('linkText', None)
    
    @property
    def linkAttributes(self):
        return self.properties.get('linkAttributes', None)
    

class ColumnColumnFormatting(ApexGroup):
    @property
    def htmlExpression(self):
        return self.properties.get('htmlExpression', None)
    

class ColumnSecurity(ApexGroup):
    @property
    def authorizationScheme(self):
        return self.properties.get('authorizationScheme', None)
    
    @property
    def escapeSpecialChars(self):
        return self.properties.get('escapeSpecialChars', None)
    
    
class Column(ApexObject):
    
    # Properties

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
    def reportColumnQueryId(self):
        return self.properties.get('reportColumnQueryId', None)

    @property
    def derivedColumn(self):
        return self.properties.get('derivedColumn', None)
    
    # Groups

    @property
    def heading(self) -> ColumnHeading:
        return self.groups.get('heading', None)

    @property
    def layout(self) -> ColumnLayout:
        return self.groups.get('layout', None)

    @property
    def appearance(self) -> ColumnAppearance:
        return self.groups.get('appearance', None)

    @property
    def source(self) -> ColumnSource:
        return self.groups.get('source', None)

    @property
    def sorting(self) -> ColumnSorting:
        return self.groups.get('sorting', None)

    @property
    def link(self) -> ColumnLink:
        return self.groups.get('link', None)

    @property
    def advanced(self) -> ColumnAdvanced:
        return self.groups.get('advanced', None)
    
    @property
    def link(self) -> ColumnLink:
        return self.groups.get('link', None)
    
    @property
    def columnFormatting(self) -> ColumnColumnFormatting:
        return self.groups.get('columnFormatting', None)

    @property
    def columnFilter(self) -> ColumnColumnFilter:
        return self.groups.get('columnFilter', None)
    
    @property
    def security(self) -> ColumnSecurity:
        return self.groups.get('security', None)
    
    @property
    def exportPrinting(self) -> ColumnExportPrinting:
        return self.groups.get('exportPrinting', None)
    

    # Child
