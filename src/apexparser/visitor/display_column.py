from ..objects import *
from . import RuleNotImplemented


class DisplayColumnVisitor:
    def visit_display_column(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        obj = DisplayColumn(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    obj.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    obj.add_group(item[0], item[1])
                else:
                    obj.add_property(item[0], item[1])
            elif isinstance(item, ApexObject):
                obj.add_child(item)
            elif item is None:
                continue
            else:
                name = f"DisplayColumn '{item.component_id}'" if isinstance(item, ApexObject) else item[1].text
                raise RuleNotImplemented(f"unprocessed: {name}")
        return obj

    def visit_display_column_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_display_column_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_display_column_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_display_column_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_display_column_identification(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('identification', DisplayColumnIdentification(d))
    
    def visit_display_column_identification_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_display_column_identification_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'column':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")