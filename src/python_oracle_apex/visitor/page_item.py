from ..objects import *
from . import RuleNotImplemented


class PageItemVisitor:

    def visit_page_item(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        page_item = PageItem(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    page_item.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    page_item.add_group(item[0], item[1])
                else:
                    page_item.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return page_item

    def visit_page_item_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_page_item_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_page_item_group_block(self, node, visited_children):
        return visited_children[0]


    def visit_page_item_label(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('label', PageItemLabel(d) )
    
    def visit_page_item_label_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_label_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'label':
                return (v[0].text, v[3])
            case 'alignment' | 'duplicateSubmissionUrl':
                return (v[0].text, v[3][0].text)
            case _:
                raise RuleNotImplemented()


    def visit_page_item_settings(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('settings', PageItemSettings(d) )
    
    def visit_page_item_settings_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_settings_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            # case 'sequence' | 'label':
            #     return (v[0].text, v[3])
            case 'trimSpaces':
                return (v[0].text, v[3][0].text)
            case _:
                raise RuleNotImplemented()

    def visit_page_item_session_state(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('sessionState', PageItemSessionState(d) )
    
    def visit_page_item_session_state_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_session_state_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            # case 'sequence' | 'label':
            #     return (v[0].text, v[3])
            case 'dataType' | 'storage':
                return (v[0].text, v[3][0].text)
            case _:
                raise RuleNotImplemented()


    def visit_page_item_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', PageItemLayout(d) )
    
    def visit_page_item_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'slot' | 'region':
                return (v[0].text, v[3])
            case 'alignment':
                return (v[0].text, v[3][0].text)
            case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_page_item_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', PageItemAppearance(d) )
    
    def visit_page_item_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'template' | 'cssClasses' | 'width' | 'valuePlaceholder':
                return (v[0].text, v[3])
            case 'templateOptions':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()

    def visit_page_item_validation(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('validation', PageItemValidation(d) )
    
    def visit_page_item_validation_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_validation_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'valueRequired' | 'maxLength':
                return (v[0].text, v[3])
            case '?':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()

    def visit_page_item_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('advanced', PageItemAdvanced(d) )
    
    def visit_page_item_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'customAttributes':
                return (v[0].text, v[3])
            case 'postText':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()


    def visit_page_item_security(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('security', PageItemSecurity(d) )
    
    def visit_page_item_security_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_security_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'encryptSessionState':
                return (v[0].text, v[3])
            case 'sessionStateProtection' | 'restrictedChars':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()
