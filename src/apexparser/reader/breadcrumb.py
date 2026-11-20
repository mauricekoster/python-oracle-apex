from ..objects import *
from . import make_entry_b
from .utils import make_properties, make_group

def make_breadcrumb(data):
    breadcrumb = Breadcrumb(data['id'])

    make_properties({
                        'name': 'name',
                    }, 
                    data, 'identification', breadcrumb
                    )

    if 'entries' in data:
        for entry in data['entries']:
            e = make_entry_b(entry)
            breadcrumb.add_child(e)
    return breadcrumb