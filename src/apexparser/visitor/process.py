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
            else:
                raise RuleNotImplemented()
        return ('source', ProcessSource(d) )

    def visit_process_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_process_source_property(self, node, visited_children):
        v = visited_children[0]
        
        title, _, _, value = v
        match title.text:
            case 'location' | 'language':
                value = value[0].text
        return (title.text, value)



    def visit_process_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('execution', ProcessExecution(d) )

    def visit_process_execution_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_process_execution_property(self, node, visited_children):
        v = visited_children[0]
        
        title, _, _, value = v
        if title.text == 'runProcess':
            value = value[0].text
        return (title.text, value)


    def visit_process_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('advanced', ProcessAdvanced(d) )

    def visit_process_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_process_advanced_property(self, node, visited_children):
        v = visited_children[0]
        
        title, _, _, value = v
        return (title.text, value)


