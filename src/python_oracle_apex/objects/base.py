class ApexGroup():
    def __init__(self, initial_data={}):
        self.properties = {}
        self.properties.update(initial_data)

    def __setitem__(self, key, value):
        self.properties[key] = value
    
    def __getitem__(self, key):
        return self.properties.get(key, None)

    def get(self, key, default=None):
        return self.properties.get(key, default)


class ApexObject():
    def __init__(self, component_id=None, initial_data={}):
        self.component_id = component_id
        self.properties = {}
        self.properties.update(initial_data)
        self.groups = {}
        self.children = []

    def __setitem__(self, key, value):
        if isinstance(value, ApexGroup):
            self.groups[key] = value
        elif isinstance(value, ApexObject):
            self.children[key] = value
        else:
            self.properties[key] = value
    
    def __getitem__(self, key):
        if key in self.groups:
            return self.groups.get(key, None)
        elif key in self.children:
            return self.children.get(key, None)
        else:
            return self.properties.get(key, None)
    
    def add_property(self, key, value):
        self.properties[key] = value
    
    def add_group(self, key, value):
        self.groups[key] = value

    def add_child(self, child):
        self.children.append(child)

  