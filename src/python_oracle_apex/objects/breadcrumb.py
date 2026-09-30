from . import ApexGroup, ApexObject


class Breadcrumb(ApexObject):
    @property
    def name(self):
        return self.properties.get('name', "<NONAME>")
