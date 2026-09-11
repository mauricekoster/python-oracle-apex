from python_oracle_apex.objects import *
from .utils import make_group, make_properties


def make_page_item_label(data):
    f = {
        'label': 'label',
        'alignment': 'alignment',
    }
    d = make_group(f, data)
    return PageItemLabel(d)

def make_page_item_layout(data):
    f = {
        'sequence': 'sequence',
        'region': 'region',
        'slot': 'slot',
        'alignment': 'alignment',
        'start-new-layout': 'startNewLayout',
        'start-new-row': 'startNewRow',
        'row-css-classes': 'rowCssClasses',
        'column': 'column',
        'new-column': 'newColumn',
        'column-span': 'columnSpan',
        'row-span': 'rowSpan',
        'label-column-span': 'labelColumnSpan',
        'column-css-classes': 'columnCssClasses',
        'column-attributes': 'columnAttributes',
    }    
    d = make_group(f, data)
    return PageItemLayout(d)

def make_page_item_appearance(data):
    return {}


def make_page_item(page_item):
    p = PageItem(page_item['id'])
    make_properties({
                'name': 'name',
                'type': 'type'
            }, 
            page_item, 'identification', p
            )

    if 'label' in page_item:
        l = make_page_item_label(page_item['label'])
        p.add_group('label',  l)
        
    if 'layout' in page_item:
        l = make_page_item_layout(page_item['layout'])
        p.add_group('layout',  l)

    if 'appearance' in page_item:
        a = make_page_item_appearance(page_item['appearance'])
        p.add_group('appearance', a)
    return p

