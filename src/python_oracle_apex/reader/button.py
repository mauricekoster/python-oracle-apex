from python_oracle_apex.objects import *
from .utils import make_group, make_properties


def make_button_layout(data):
    f = {
        'sequence': 'sequence',
        'region': 'region',
        'slot': 'slot',
        'column': 'column',
        'alignment': 'alignment',
        'new-column': 'newColumn',
        'column-span': 'columnSpan',
        'start-new-layout': 'startNewLayout',
        'start-new-row': 'startNewRow',

    }
    d = make_group(f, data)
    return ButtonLayout(d)

def make_button(data):
    b = Button(data['id'])
    make_properties({
        'button-name': 'buttonName',
        'label': 'label'
    }, data, 'identification', b)

    if 'layout' in data:
        l = make_button_layout(data['layout'])
        b.add_group('layout', l)

    return b
