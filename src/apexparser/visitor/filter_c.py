from ..objects import *
from . import RuleNotImplemented


class FilterCVisitor:
    def visit_filter_c(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        obj = Filter(component_id, variant='filter_c')
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
                name = f"Filter '{item.component_id}'" if isinstance(item, ApexObject) else item[1].text
                raise RuleNotImplemented(f"unprocessed: {name}")
        return obj

    def visit_filter_c_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_filter_c_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_filter_c_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        if type(value) is list:
            return (title.text, value[0].text)
        else:
            return (title.text, value)

    def visit_filter_c_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_filter_c_child_component(self, node, visited_children):
        return visited_children[0]

    def visit_filter_c_label(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('label', FilterLabel(d))
    
    def visit_filter_c_label_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_filter_c_label_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'label':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_filter_c_lov(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('lov', FilterLov(d))
    
    def visit_filter_c_lov_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_filter_c_lov_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_filter_c_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('layout', FilterLayout(d))
    
    def visit_filter_c_layout_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_filter_c_layout_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_filter_c_suggestions(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('suggestions', FilterSuggestions(d))
    
    def visit_filter_c_suggestions_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_filter_c_suggestions_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            # case '':
            #     return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_filter_c_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', FilterSource(d))
    
    def visit_filter_c_source_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_filter_c_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'databaseColumn':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")