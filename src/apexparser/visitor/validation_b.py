from ..objects import *
from . import RuleNotImplemented


class ValidationBVisitor:
    def visit_validation_b(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        obj = Validation(component_id)
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
                name = f"Validation '{item.component_id}'" if isinstance(item, ApexObject) else item[1].text
                raise RuleNotImplemented(f"unprocessed: {name}")
        return obj

    def visit_validation_b_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_validation_b_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_validation_b_direct_property(self, node, visited_children):
        v = visited_children
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_validation_b_group_block(self, node, visited_children):
        return visited_children[0]
