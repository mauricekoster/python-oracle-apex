from ..objects import *
from . import RuleNotImplemented


class FacetVisitor:

    def visit_facet(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        facet = Facet(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    facet.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    facet.add_group(item[0], item[1])
                else:
                    facet.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return facet

    def visit_facet_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_facet_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_facet_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_facet_label(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('label', FacetLabel(d) )
    
    def visit_facet_label_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_label_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'label' | 'showLabelForCurrentFacet':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_facet_lov(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('lov', FacetLov(d) )
        
    def visit_facet_lov_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_lov_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_facet_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', FacetLayout(d) )
        
    def visit_facet_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_facet_list_entries(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('list-entries', FacetListEntries(d) )
        
    def visit_facet_list_entries_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_list_entries_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'maxDisplayedEntries' | 'sortByTopCounts':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_facet_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('source', FacetSource(d) )
        
    def visit_facet_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_facet_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'databaseColumn':
                return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()
    