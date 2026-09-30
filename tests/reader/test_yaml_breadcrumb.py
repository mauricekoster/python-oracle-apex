from python_oracle_apex import *
import yaml
from python_oracle_apex.reader import make_breadcrumb


def load_data(input):
    return yaml.safe_load(input, comments=True)


def test_breadcrumb_identification():
    data = load_data(
"""---
id: 4442603438704883
identification: 
  name: Breadcrumb

""")

    b = make_breadcrumb(data)
    assert isinstance(b, Breadcrumb)

    assert b.name == 'Breadcrumb'


def test_yaml_breadcrumb_entry():
    data = load_data(
"""---
id: 4442603438704883
identification: 
  name: Breadcrumb


entries: 
  - # ====== Entry: Overzicht zaken bij typeringen ===============
    id: 3536800658881044
    identification: 
      name: Overzicht
      page-number: 1234

    execution: 
      sequence: 10

    link: 
      target: 
        url: 'f?p=&APP_ID.:6370:&APP_SESSION.::&DEBUG.:::'
        page: 1234 # Overzicht
""")        
    b = make_breadcrumb(data)
    assert isinstance(b, Breadcrumb)

    assert b.name == 'Breadcrumb'