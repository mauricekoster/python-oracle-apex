from python_oracle_apex import *
import yaml
from python_oracle_apex.reader import make_page


def load_data(input):
    return yaml.safe_load(input, comments=True)


def test_page_identification():
    data = load_data(
"""---
id: 1111
identification: 
  name: Page
  alias: PAGE
  title: 'Nice page'

""")

    p = make_page(data)
    assert isinstance(p, Page)

    assert p.name == 'Page'
    assert p.alias == 'PAGE'
    assert p.title == 'Nice page'
    assert p.page == 1111


def test_page_unknown_property_is_ignored():
    data = load_data(
"""---
id: 1111
identification: 
  name: Page
  unknown: Unknown
""")

    p = make_page(data)
    assert isinstance(p, Page)


def test_page_property_with_comment():
    data = load_data(
"""---
id: 1111
identification: 
  name: Page
  alias: PAGE # comment
""")

    p = make_page(data)
    assert isinstance(p, Page)

    assert p.alias == "PAGE@comment"
