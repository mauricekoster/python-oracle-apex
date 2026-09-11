from python_oracle_apex.objects import *

def make_properties(mapper, data, section, object: ApexObject):
    for field_src, field_dest in mapper.items():
        if field_src in data[section]:
            comment = data[section].get_comment(field_src)
            value = data[section][field_src]
            if comment:
                value = value + '@' + comment.inline.value
            object.add_property(field_dest, value)

def make_group(mapper, data):
    d = {}
    for k, v in data.items():
        comment = data.get_comment(k)
        if comment:
            v = v + '@' + comment.inline.value
        if k in mapper:
            d[mapper[k]] = v
        else:
            raise AttributeError(f"Unknown property '{k}'")
    return d
