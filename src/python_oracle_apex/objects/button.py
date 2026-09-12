from . import ApexGroup, ApexObject


class ButtonLayout(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

    @property
    def sequence(self):
        return self.properties.get('sequence', None)

    @property
    def region(self):
        return self.properties.get('region', None)


class ButtonAppearance(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)

class ButtonBehavior(ApexGroup):
    def __init__(self, initial_data={}):
        super().__init__(initial_data)



class Button(ApexObject):
    def __init__(self, component_id=None, initial_data={}):
        super().__init__(component_id, initial_data)

    @property
    def button_name(self):
        return self.properties.get('buttonName', None)

    @property
    def label(self):
        return self.properties.get('label', None)

    @property
    def layout(self):
        return self.groups.get('layout', ButtonLayout({}))

