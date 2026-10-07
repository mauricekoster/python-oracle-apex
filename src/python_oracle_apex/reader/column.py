from python_oracle_apex.objects import *
from .utils import make_group, make_properties



def make_column_heading(heading):
    d = make_group({
        'heading': 'heading',
        'alignment': 'alignment'
    }, heading)
    return ColumnHeading(d)

def make_column(column):
    c = Column(str(column['id']))
    make_properties({
                    'column-name': 'columnName',
                    'type': 'type'
                }, 
                column, 'identification', c
                )

    if 'heading' in column:
        h = make_column_heading(column['heading'])
        c.add_group('heading', h)

    return c