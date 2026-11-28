from ..objects import *
from . import RuleNotImplemented


class ColumnVisitor:

    def visit_column(self, node, visited_children):
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
            else: # pragma: no cover
                raise RuleNotImplemented(f"unprocessed: {item}")
        return act

    def visit_column_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_column_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_column_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_column_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('layout', ColumnLayout(d) )
    
    def visit_column_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'group':
                return (v[0].text, v[3])
            case 'columnAlignment':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_column_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('appearance', ColumnAppearance(d) )
    
    def visit_column_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'cssClasses' | 'formatMask' | 'backgroundColor' | 'foregroundColor' | 'barWidth' | 'downloadText' | 'width' | 'height' | 'template' | 'group':
                return (v[0].text, v[3])
            case 'viewFileAs':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', ColumnSource(d) )
    
    def visit_column_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_column_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'primaryKey' | 'dataType' | 'availableOnClient' | 'valueProtected' | 'timezoneAware' | 'databaseColumn' | 'sqlExpression':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_heading(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('heading', ColumnHeading(d))
    
    def visit_column_heading_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_heading_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'heading' | 'alternativeLabel':
                return (v[0].text, v[3])
            case 'alignment':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('advanced', ColumnAdvanced(d))
    
    def visit_column_advanced_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'htmlDomId' | 'endUserAlias' | 'cssClasses' | 'computeSum' | 'customAttributes' | 'cellWidth':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_link(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('link', ColumnLink(d))
    
    def visit_column_link_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_link_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'target' | 'linkText' | 'linkAttributes':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_column_formatting(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('columnFormatting', ColumnColumnFormatting(d))
    
    def visit_column_column_formatting_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_column_formatting_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'htmlExpression':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_security(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('security', ColumnSecurity(d))
    
    def visit_column_security_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_security_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'authorizationScheme' | 'escapeSpecialChars':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_column_formatting(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('columnFormatting', ColumnColumnFormatting(d))
    
    def visit_column_column_formatting_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_column_formatting_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'htmlExpression':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_column_sorting(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('sorting', ColumnSorting(d))
    
    def visit_column_sorting_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_column_sorting_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sortable':
                return (v[0].text, v[3])
            case 'direction':
                return (v[0].text, v[3].text)
            case 'defaultSequence':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")