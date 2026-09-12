from ..objects import *
from . import RuleNotImplemented


class DynamicActionVisitor:

    def visit_dynamic_action(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        dynact = DynamicAction(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    dynact.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    dynact.add_group(item[0], item[1])
                else:
                    dynact.add_property(item[0], item[1])
            elif isinstance(item, ApexObject):
                dynact.add_child(item)
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return dynact

    def visit_dynamic_action_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_dynamic_action_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_dynamic_action_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_dynamic_action_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_dynamic_action_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('execution', DynamicActionExecution(d) )
    
    def visit_dynamic_action_execution_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_dynamic_action_execution_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence':
                    return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()
            
    def visit_dynamic_action_when(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('when', DynamicActionWhen(d) )
    
    def visit_dynamic_action_when_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_dynamic_action_when_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'event':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_dynamic_action_client_side_condition(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('clientSideCondition', DynamicActionClientSideCondition(d) )
    
    def visit_dynamic_action_client_side_condition_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_dynamic_action_client_side_condition_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'event' | 'javaScriptExpression':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

