from ..objects import *
from . import RuleNotImplemented

class PageVisitor:
    def visit_page_object(self, node, visited_children):
        """ Gets the section name. """
        component_id = visited_children[2]
        body_parts = visited_children[5]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        page = Page(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    page.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    page.add_group(item[0], item[1])
                else:
                    page.add_property(item[0], item[1])
            elif isinstance(item, ApexObject):
                page.add_child(item)
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return page


    def visit_page_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_page_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_page_child_component(self, node, visited_children):
        return visited_children[0]


    def visit_page_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)


    def visit_page_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', PageAppearance(d))

    def visit_page_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_appearance_property(self, node, visited_children):
        v = visited_children[0]
        return (v[0].text, v[3])


    def visit_page_navigation(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('navigation', PageNavigation(d))
    
    def visit_page_navigation_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_navigation_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'cursorFocus':
                return (v[0].text, v[3][0].text)
            case 'warnOnUnsavedChanges':
                return (v[0].text, v[3])


    def visit_page_css(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('css', PageCss(d))

    def visit_page_css_property_line(self, node, visited_children):
        return visited_children[1]


    def visit_page_css_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'inline':
                return (v[0].text, v[-1])
            case 'fileUrls':
                return (v[0].text, v[3])

    def visit_page_security(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('security', PageSecurity(d))

    def visit_page_security_property_line(self, node, visited_children):
        return visited_children[1]


    def visit_page_security_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'authentication' | 'pageAccessProtection':
                return (v[0].text, v[3][0].text)
            case 'formAutoComplete':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_page_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('advanced', PageAdvanced(d))

    def visit_page_advanced_property_line(self, node, visited_children):
        return visited_children[1]


    def visit_page_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'reloadOnSubmit' | 'duplicateSubmissionUrl':
                return (v[0].text, v[3][0].text)
            case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_page_help(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('help', PageHelp(d))
    
    def visit_page_help_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_help_property(self, node, visited_children):
        v = visited_children[0]
        return (v.text, visited_children[3])
