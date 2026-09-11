from ..objects import *
from . import make_region, make_page_item, make_button
from .utils import make_properties


def make_page(data):
    page = Page(data['id'])
    make_properties({
                    'name': 'name',
                    'title': 'title',
                    'alias': 'alias'
                }, 
                data, 'identification', page
                )

    if 'regions' in data:
        for region in data['regions']:
            r = make_region(region)
            page.add_child(r)

    if 'page-items' in data:
        for page_item in data['page-items']:
            p = make_page_item(page_item)
            page.add_child(p)

    if 'buttons' in data:
        for button in data['buttons']:
            b = make_button(button)
            page.add_child(b)

    return page
