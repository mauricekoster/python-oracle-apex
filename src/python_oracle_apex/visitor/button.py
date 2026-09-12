from ..objects import *
from . import RuleNotImplemented


class ButtonVisitor:

    def visit_button(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        button = Button(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    button.add_group(item[0], item[1])
                elif isinstance(item[1], ApexGroup):
                    button.add_group(item[0], item[1])
                else:
                    button.add_property(item[0], item[1])
            elif item is None:
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return button

    def visit_button_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_button_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_button_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_button_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_button_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', ButtonLayout(d) )
    
    def visit_button_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_button_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            # case 'sequence' | 'slot' | 'region':
            #     return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()


    def visit_button_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', ButtonAppearance(d) )
    
    def visit_button_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_button_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'buttonTemplate' | 'hot' | 'icon':
                 return (v[0].text, v[3])
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'templateOptions' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case 'templateOptions':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()

    def visit_button_behavior(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('behavior', ButtonBehavior(d) )
    
    def visit_button_behavior_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_button_behavior_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'target' | 'action':
                return (v[0].text, v[3][0])
            case 'warnOnUnsavedChanges':
                return (v[0].text, v[3].text)
            # case 'alignment':
            #     return (v[0].text, v[3][0].text)
            # case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
            #     return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

