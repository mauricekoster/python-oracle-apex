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
            else: # pragma: no cover
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
            else: # pragma: no cover
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
            case _: # pragma: no cover
                raise RuleNotImplemented()


    def visit_page_item_settings(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('settings', PageItemSettings(d) )
    
    def visit_page_item_settings_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_settings_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'showControls' | 'valueProtected' | 'minValue' | 'maxValue' | 'executeValidations':
                return (v[0].text, v[3])
            case 'trimSpaces' | 'numberAlignment' | 'virtualKeyboard' | 'pageActionOnSelection':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_session_state(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
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
            case _: # pragma: no cover
                raise RuleNotImplemented()


    def visit_page_item_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('layout', PageItemLayout(d) )
    
    def visit_page_item_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'slot' | 'region' | 'startNewRow' | 'labelColumnSpan':
                return (v[0].text, v[3])
            case 'alignment':
                return (v[0].text, v[3][0].text)
            case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('appearance', PageItemAppearance(d) )
    
    def visit_page_item_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'template' | 'cssClasses' | 'templateOptions' | 'width' | 'valuePlaceholder' | 'height' | 'width' | 'formatMask':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_validation(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
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
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_page_item_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('advanced', PageItemAdvanced(d) )
    
    def visit_page_item_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'customAttributes' | 'cssClasses':
                return (v[0].text, v[3])
            case 'postText':
                return (v[0].text, v[3][0])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")


    def visit_page_item_security(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
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
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_page_item_lov(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('lov', PageItemLov(d) )
    
    def visit_page_item_lov_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_lov_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'lov' | 'displayNullValue' | 'nullDisplayValue' | 'sqlQuery' | 'displayExtraValues':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_default(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('default', PageItemDefault(d) )
    
    def visit_page_item_default_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_page_item_default_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'staticValue' | 'sqlQuerySingleValue':
                return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', PageItemSource(d))
    
    def visit_page_item_source_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_page_item_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'databaseColumn' | 'plsqlFunctionBody' | 'sqlQuery' | 'staticValue':
                return (v[0].text, v[3])
            case 'type' | 'used':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_server_side_condition(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('serverSideCondition', PageItemServerSideCondition(d))
    
    def visit_page_item_server_side_condition_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_page_item_server_side_condition_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type' | 'sqlQuery':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_page_item_help(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('help', PageItemHelp(d))
    
    def visit_page_item_help_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_page_item_help_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'inlineHelpText' | 'helpText':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")