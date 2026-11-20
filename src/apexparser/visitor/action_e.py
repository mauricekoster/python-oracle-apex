from ..objects import *
from . import RuleNotImplemented


class ActionEVisitor:

    def visit_action_e(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        act = Action(component_id)
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

    def visit_action_e_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_action_e_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_e_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_action_e_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_action_e_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', ActionLayout(d) )
    
    def visit_action_e_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_e_layout_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_action_e_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', ActionAppearance(d) )
    
    def visit_action_e_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_e_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'icon' | 'hot' | 'cssClasses' | 'showAsDisabled':
                return (v[0].text, v[3])
            case 'displayType':
                return (v[0].text, v[3][0].text)
            case _:
                raise RuleNotImplemented()

    def visit_action_e_behavior(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('behavior', ActionBehavior(d) )
    
    def visit_action_e_behavior_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_e_behavior_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'target' | 'targetUrl' | 'linkAttributes':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _:
                raise RuleNotImplemented()
