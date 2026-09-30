from ..objects import *
from .utils import make_properties, make_group


def make_entry_b_execution(data):
    d = make_group({
        'sequence': 'sequence'
    }, data)
    return EntryBExecution(d)


def make_entry_b_link(data):
    d = make_group({
        'target': 'target'
    }, data)
    return EntryBLink(d)


def make_entry_b(data):
    e = EntryB(data['id'])

    make_properties({
                        'name': 'name',
                        'page-number': 'pageNumber'
                    }, 
                    data, 'identification', e
                    )

    if 'execution' in data:
        g = make_entry_b_execution(data['execution'])
        e.add_group('execution',  g)

    if 'link' in data:
        g = make_entry_b_link(data['link'])
        e.add_group('link',  g)

    return e