from . import ApexGroup, ApexObject, EntryB


class Breadcrumb(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', "<NONAME>")

    @property
    def entries(self) -> list[EntryB]:
        return [x for x in self.children if isinstance(x, EntryB)]

    def get_by(self, property_name, search_value):
        items = [x for x in self.entries if x.properties[property_name] == search_value]
        if items:
            return items[0]
        else:
            return None
