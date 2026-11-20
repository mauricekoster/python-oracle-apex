class ApexGroup():
    def __init__(self, initial_data={}):
        self.properties = {}
        self.properties.update(initial_data)


class ApexObject():
    def __init__(self, component_id=None, initial_data={}, variant=None):
        self.component_id = component_id
        self.variant = variant
        self.properties = {}
        self.properties.update(initial_data)
        self.groups = {}
        self.children = []
    
    def add_property(self, key, value):
        self.properties[key] = value
    
    def add_group(self, key, value):
        self.groups[key] = value

    def add_child(self, child):
        self.children.append(child)

  