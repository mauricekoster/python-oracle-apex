from ..objects import *
from . import RuleNotImplemented


class SeriesVisitor:
    def visit_series(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        proc = Series(component_id)
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

    def visit_series_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_series_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_series_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_series_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_series_execution(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('execution', SeriesExecution(d))
    
    def visit_series_execution_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_series_execution_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_series_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', SeriesSource(d))
    
    def visit_series_source_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_series_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            #case '':
            #    return (v[0].text, v[3])
            case 'location':
               return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_series_column_mapping(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('columnMapping', SeriesColumnMapping(d))
    
    def visit_series_column_mapping_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_series_column_mapping_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'label' | 'value':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_series_line(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('line', SeriesLine(d))
    
    def visit_series_line_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_series_line_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'width':
                return (v[0].text, v[3])
            case 'type' | 'style':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")