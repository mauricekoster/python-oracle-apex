from pathlib import Path
import yaml

from python_oracle_apex.objects import *

from . import make_page

"""
Read YAML and transform to Page object.

Property names will be translated to the names used in de APEX Lang spec. (version 26.1)
"""



def parse_page_file(fn: Path) -> Page:

    with fn.open('r') as f:
        data = yaml.safe_load(f, comments=True)


    return make_page(data)


