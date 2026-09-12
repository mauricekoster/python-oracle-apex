from . import ApexGroup, ApexObject


class PageItemLabel(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def label(self):
        return self.properties.get('label', None) 


class PageItemSettings(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)


class PageItemLayout(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def region(self):
        return self.properties.get('region', None)


class PageItemAppearance(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

class PageItemValidation(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)

class PageItemAdvanced(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)

class PageItemSessionState(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)

class PageItemSecurity(ApexGroup):
    def __init__(self, initial_data={}):
            super().__init__(initial_data)


class PageItem(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    @property
    def name(self):
        return self.properties.get('name', self.component_id)

    @property
    def type(self):
        return self.properties.get('type', None)


    @property
    def layout(self):
        return self.groups.get('layout', PageItemLayout())

    @property
    def label(self):
        return self.groups.get('label', PageItemLabel())
    
