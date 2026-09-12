from ..objects import *
from . import RuleNotImplemented


class ActionCVisitor:

    def visit_action_c(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        act = ActionC(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    act.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    act.add_group(item[0], item[1])
                else:
                    act.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return act

    def visit_action_c_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_action_c_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_c_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_action_c_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_action_c_affected_elements(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('affectedElements', ActionCAffectedElements(d) )
    
    def visit_action_c_affected_elements_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_c_affected_elements_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'selectionType' | 'items':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_action_c_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('execution', ActionCExecution(d) )
    
    def visit_action_c_execution_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_c_execution_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'fireWhenEventResultIs':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()
