from ..objects import *
from . import RuleNotImplemented


class AxisVisitor:
    def visit_axis(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        proc = Axis(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    proc.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    proc.add_group(item[0], item[1])
                else:
                    proc.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return proc

    def visit_axis_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_axis_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_axis_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_axis_group_block(self, node, visited_children):
        return visited_children[0]


    def visit_axis_value(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('value', AxisValue(d))
    
    def visit_axis_value_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_axis_value_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'min' | 'max' | 'decimalPlaces' | 'currency' | 'pattern' | 'step':
                return (v[0].text, v[3])
            case 'format' | 'formatScaling' | 'baselineScaling' | 'scale':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_axis_minor_ticks(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('minorTicks', AxisMinorTicks(d))
    
    def visit_axis_minor_ticks_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_axis_minor_ticks_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'step':
                return (v[0].text, v[3])
            case 'show':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")