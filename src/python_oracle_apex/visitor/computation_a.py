from ..objects import *
from . import RuleNotImplemented


class ComputationAVisitor:
    def visit_computation_a(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        computation_a = ComputationA(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    computation_a.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    computation_a.add_group(item[0], item[1])
                else:
                    computation_a.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return computation_a

    def visit_computation_a_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_computation_a_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_computation_a_direct_property(self, node, visited_children):
        v = visited_children
        title, _, _, value = v
        return (title.text, value)

    def visit_computation_a_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_computation_a_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('execution', ComputationAExecution(d) )
    
    def visit_computation_a_execution_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_computation_a_execution_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case 'point':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_computation_a_computation(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('execution', ComputationAComputation(d) )
    
    def visit_computation_a_computation_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_computation_a_computation_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'staticValue':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

