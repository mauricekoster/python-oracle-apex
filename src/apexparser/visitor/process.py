from ..objects import *
from . import RuleNotImplemented


class ProcessVisitor:
    def visit_process(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        proc = Process(component_id)
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

    def visit_process_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_process_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_process_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_process_group_block(self, node, visited_children):
        return visited_children[0]
    
    def visit_process_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', ProcessSource(d))
    
    def visit_process_source_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'remoteServer' | 'plsqlCode' | 'tableName' | 'pkColumn' | 'pkItem':
                return (v[0].text, v[3])
            case 'location' | 'language':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")


    def visit_process_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('execution', ProcessExecution(d))
    
    def visit_process_execution_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_execution_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'point':
                return (v[0].text, v[3])
            case 'runProcess':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")


    def visit_process_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('advanced', ProcessAdvanced(d))
    
    def visit_process_advanced_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'staticId' | 'executionMappingIdentifier':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_process_target(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('target', ProcessTarget(d))
    
    def visit_process_target_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_target_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'tableName' | 'pkColumn' | 'pkItem' | 'returnKeyIntoItem':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_process_success_message(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('successMessage', ProcessSuccessMessage(d))
    
    def visit_process_success_message_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_success_message_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'successMessage':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_process_error(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('error', ProcessError(d))
    
    def visit_process_error_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_error_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'errorMessage':
                return (v[0].text, v[3])
            case 'displayLocation':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_process_server_side_condition(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('serverSideCondition', ProcessServerSideCondition(d))
    
    def visit_process_server_side_condition_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_process_server_side_condition_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type' | 'value' | 'whenButtonPressed' | 'item':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")