from ..objects import *
from . import RuleNotImplemented


class SortAVisitor:
    def visit_sort_a(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        obj = Sort(component_id, variant='sort_a')
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
                name = f"Sort '{item.component_id}'" if isinstance(item, ApexObject) else item[1].text
                raise RuleNotImplemented(f"unprocessed: {name}")
        return obj

    def visit_sort_a_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_sort_a_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_sort_a_direct_property(self, node, visited_children):
        v = visited_children
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_sort_a_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_sort_a_sort(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('sort', SortSort(d))
    
    def visit_sort_a_sort_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_sort_a_sort_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case 'direction' | 'nulls':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")