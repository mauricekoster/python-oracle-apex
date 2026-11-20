from ..objects import *
from . import RuleNotImplemented


class ColumnFVisitor:

    def visit_column_f(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        act = Column(component_id)
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

    def visit_column_f_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_column_f_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_f_direct_property(self, node, visited_children):
        # v = visited_children[0]    # use this if more than one properties
        v = visited_children
        title, _, _, value = v
        return (title.text, value)

    def visit_column_f_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_column_f_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', ColumnLayout(d) )
    
    def visit_column_f_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_f_layout_property(self, node, visited_children):
        v = visited_children
        # v = visited_children[0]
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_column_f_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', ColumnAppearance(d) )
    
    def visit_column_f_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_f_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'group' | 'formatMask':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_column_f_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('source', ColumnSource(d) )
    
    def visit_column_f_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_f_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'databaseColumn' | 'sqlExpression' | 'primaryKey' | 'availableOnClient' | 'valueProtected':
                return (v[0].text, v[3])
            case 'dataType' | 'type':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    