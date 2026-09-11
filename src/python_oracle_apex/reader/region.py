from python_oracle_apex.objects import *
from .utils import make_group, make_properties


def make_region_layout(data):
    f = {
        'sequence': 'sequence',
        'parent-region': 'parentRegion',
        'slot': 'slot',
        'start-new-layout': 'startNewLayout',
        'start-new-row': 'startNewRow',
        'column': 'column',
        'new-column': 'newColumn',
        'column-span': 'columnSpan'
    }    
    d = make_group(f, data)
    return RegionLayout(d)



def make_region_appearance(data):
    f = {
        'icon': 'icon',
        'template': 'template',
        'template-options': 'templateOptions',
        'render-components': 'renderComponents',
        'css-classes': 'cssClasses',
    }    
    d = make_group(f, data)
    return RegionAppearance(d)


def make_region(region) -> Region:
    r = Region(region['id'])
    make_properties({
                    'name': 'name',
                    'title': 'title',
                    'type': 'type'
                }, 
                region, 'identification', r
                )

    if 'layout' in region:
        l = make_region_layout(region['layout'])
        r.add_group('layout',  l)

    if 'appearance' in region:
        a = make_region_appearance(region['appearance'])
        r.add_group('appearance', a)
    return r
