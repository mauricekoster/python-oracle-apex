from . import ApexGroup, ApexObject, Region, PageItem, Button, DynamicAction, Process

class PageAppearance(ApexGroup):
    @property
    def pageMode(self):
        return self.properties.get('pageMode', None)
    
    @property
    def pageTemplate(self):
        return self.properties.get('pageTemplate', None)
    
    @property
    def dialogTemplate(self):
        return self.properties.get('dialogTemplate', None)

    @property
    def templateOptions(self):
        return self.properties.get('templateOptions', None)

    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)

    @property
    def mediaType(self):
        return self.properties.get('mediaType', None)


class PageNavigation(ApexGroup):
    @property
    def cursorFocus(self):
        return self.properties.get('cursorFocus', None)

    @property
    def warnOnUnsavedChanges(self):
        return self.properties.get('warnOnUnsavedChanges', None)


class PageHtmlHeader(ApexGroup):
    @property
    def htmlHeader(self):
        return self.properties.get('htmlHeader', None)

    @property
    def pageHtmlBodyAttribute(self):
        return self.properties.get('pageHtmlBodyAttribute', None)


class PageCss(ApexGroup):
    pass

class PageSecurity(ApexGroup):
    @property
    def authorizationScheme(self):
        return self.properties.get('authorizationScheme', None)

    @property
    def authentication(self):
        return self.properties.get('authentication', None)

    @property
    def deepLinking(self):
        return self.properties.get('deepLinking', None)

    @property
    def pageAccessProtection(self):
        return self.properties.get('pageAccessProtection', None)

    @property
    def formAutoComplete(self):
        return self.properties.get('formAutoComplete', None)

    @property
    def browserCache(self):
        return self.properties.get('browserCache', None)


class PageAdvanced(ApexGroup):
    @property
    def enableMetaTags(self):
        return self.properties.get('enableMetaTags', None)

    @property
    def enableDuplicatePageSubmissions(self):
        return self.properties.get('enableDuplicatePageSubmissions', None)
    
    @property
    def reloadOnSubmit(self):
        return self.properties.get('reloadOnSubmit', None)
    
    @property
    def duplicateSubmissionUrl(self):
        return self.properties.get('duplicateSubmissionUrl', None)


class PageHelp(ApexGroup):
    @property
    def helpText(self):
        return self.properties.get('helpText', None)

class PageJavaScript(ApexGroup):
    @property
    def fileUrls(self):
        return self.properties.get('fileUrls', None)
    
    @property
    def executeWhenPageLoads(self):
        return self.properties.get('executeWhenPageLoads', None)
    
    @property
    def functionAndGlobalVariableDeclaration(self):
        return self.properties.get('functionAndGlobalVariableDeclaration', None)
    
    @property
    def includeStandardJavaScriptAndCss(self):
        return self.properties.get('includeStandardJavaScriptAndCss', None)


class PageDialog(ApexGroup):
    @property
    def resizable(self):
        return self.properties.get('resizable', None)
    
    @property
    def width(self):
        return self.properties.get('width', None)
    
    @property
    def height(self):
        return self.properties.get('height', None)
    
    @property
    def maxWidth(self):
        return self.properties.get('maxWidth', None)
    
    @property
    def resizable(self):
        return self.properties.get('resizable', None)
    
    @property
    def attributes(self):
        return self.properties.get('attributes', None)
    
    @property
    def cssClasses(self):
        return self.properties.get('cssClasses', None)
    
    @property
    def chained(self):
        return self.properties.get('chained', None)
    

class PageConfig(ApexGroup):
    @property
    def buildOption(self):
        return self.properties.get('buildOption', None)
    
    


class Page(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    def __str__(self):
        return f"Page<#{self.page} name: {self.name}>"

    # Properties

    @property
    def page(self):
        return self.properties.get('page', self.component_id)

    @property
    def name(self):
        return self.properties.get('name', "<NONAME>")

    @property
    def title(self):
        return self.properties.get('title', None)

    @property
    def alias(self):
        return self.properties.get('alias', None)

    # Groups

    @property
    def appearance(self) -> PageAppearance:
        return self.groups.get('appearance', None)

    @property
    def navigation(self) -> PageNavigation:
        return self.groups.get('navigation', None)

    @property
    def htmlHeader(self) -> PageHtmlHeader:
        return self.groups.get('htmlHeader', None)

    @property
    def security(self) -> PageSecurity:
        return self.groups.get('security', None)

    @property
    def help(self) -> PageHelp:
        return self.groups.get('help', None)

    @property
    def advanced(self) -> PageAdvanced:
        return self.groups.get('advanced', None)

    @property
    def javaScript(self) -> PageJavaScript:
        return self.groups.get('javaScript', None)
    
    @property
    def dialog(self) -> PageDialog:
        return self.groups.get('dialog', None)
    
    @property
    def config(self) -> PageConfig:
        return self.groups.get('config', None)
    

    # Children

    @property
    def regions(self) -> list[Region]:
        return [x for x in self.children if isinstance(x, Region)]
    
    @property
    def page_items(self):
        return [x for x in self.children if isinstance(x, PageItem)]

    @property
    def buttons(self):
        return [x for x in self.children if isinstance(x, Button)]

    @property
    def dynamic_actions(self):
        return [x for x in self.children if isinstance(x, DynamicAction)]

    @property
    def processes(self):
        return [x for x in self.children if isinstance(x, Process)]


    def get_region(self, reference_or_name):
        regions = [x for x in self.regions 
                   if str(x.component_id)==str(reference_or_name[1:])
                   or x.name==reference_or_name
                   ]
        if len(regions) == 1:
            return regions[0]
        elif len(regions) == 0:
            return None

        return regions
