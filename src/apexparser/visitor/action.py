from ..objects import *
from . import RuleNotImplemented


class ActionVisitor:

    def visit_action(self, node, visited_children):
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
            elif isinstance(item, ApexObject):
                act.add_child(item)
            elif item is None:
                continue
            else: # pragma: no cover
                raise RuleNotImplemented(f"unprocessed: {item}")
        return act

    def visit_action_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_action_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_action_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_action_affected_elements(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('affectedElements', ActionAffectedElements(d) )
    
    def visit_action_affected_elements_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_affected_elements_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'selectionType' | 'items' | 'region' | 'columns' | 'button' | 'domObject' | 'jquerySelector' | 'javaScriptExpression':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_action_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('appearance', ActionAppearance(d) )
    
    def visit_action_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'icon' | 'hot' | 'cssClasses' | 'showAsDisabled':
                return (v[0].text, v[3])
            case 'displayType':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_action_behavior(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('behavior', ActionBehavior(d) )
    
    def visit_action_behavior_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_behavior_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'target' | 'targetUrl' | 'linkAttributes':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_action_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('execution', ActionExecution(d) )
    
    def visit_action_execution_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_execution_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'fireOnInit' | 'fireWhenEventResultIs' | 'stopExecutionOnError' | 'waitForResult':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_action_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('layout', ActionLayout(d) )
    
    def visit_action_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case 'position':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented()


    def visit_action_settings(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('settings', ActionSettings(d) )
    
    def visit_action_settings_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_action_settings_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sqlQuery' | 'itemsToSubmit' | 'plsqlCode':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented()