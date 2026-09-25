from . import ApexGroup, ApexObject, Region, PageItem, Button, DynamicAction, Process

class PageAppearance(ApexGroup):
    pass

class PageNavigation(ApexGroup):
    pass

class PageCss(ApexGroup):
    pass

class PageSecurity(ApexGroup):
    pass

class PageAdvanced(ApexGroup):
    pass

class PageHelp(ApexGroup):
    @property
    def helpText(self):
        return self['helpText']

class Page(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    def __str__(self):
        return f"Page<#{self.page} name: {self.name}>"

    @property
    def page(self):
        return self.properties.get('page', self.component_id)

    @property
    def name(self):
        return self.properties.get('name', "<NONAME>")

    @property
    def title(self):
        return self.properties['title']

    @property
    def alias(self):
        return self.properties['alias']


    @property
    def appearance(self) -> PageAppearance:
        return self.groups.get('appearance', None)

    @appearance.setter
    def appearance(self, value):
        self.groups['appearance'] = value

    @property
    def help(self) -> PageHelp:
        return self.groups.get('help', None)


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
