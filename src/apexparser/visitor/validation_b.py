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

        obj = Validation(component_id, variant='validation_b')
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

    def visit_validation_b_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('execution', ValidationExecution(d))
    
    def visit_validation_b_execution_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_validation_b_execution_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_validation_b_validation(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('validation', ValidationValidation(d))
    
    def visit_validation_b_validation_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_validation_b_validation_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'plsqlFunctionBody':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_validation_b_error(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('error', ValidationError(d))
    
    def visit_validation_b_error_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_validation_b_error_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'errorMessage' | 'associatedItem' | 'associatedColumn':
                return (v[0].text, v[3])
            case 'displayLocation':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_validation_b_server_side_condition(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('serverSideCondition', ValidationServerSideCondition(d))
    
    def visit_validation_b_server_side_condition_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_validation_b_server_side_condition_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type' | 'value':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")