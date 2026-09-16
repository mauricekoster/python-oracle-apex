from ..objects import *
from . import RuleNotImplemented


class RegionVisitor:

    def visit_region(self, node, visited_children):
        component_id = visited_children[2]
        body_parts = visited_children[6]
        if type(component_id) is list:
            component_id = component_id[0][1]
        else:
            component_id = None

        region = Region(component_id)
        for item in body_parts:
            if type(item) is tuple:
                if type(item[1]) is dict:
                    region.add_group(item[0], item[1])
                else:
                    region.add_property(item[0], item[1])
            elif item is None:
                # blanklines
                continue
            else:
                raise RuleNotImplemented(f"unprocessed: {item}")
        return region

    def visit_region_body_line(self, node, visited_children):
        return visited_children[0]

    def visit_region_direct_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_direct_property(self, node, visited_children):
        v = visited_children[0]
        title, _, _, value = v
        return (title.text, value)

    def visit_region_group_block(self, node, visited_children):
        return visited_children[0]

    def visit_region_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('layout', RegionLayout(d) )
    
    def visit_region_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'slot':
                return (v[0].text, v[3])
            case 'reloadOnSubmit' | 'duplicateSubmissionUrl':
                return (v[0].text, v[3][0].text)
            case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_region_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('appearance', RegionAppearance(d))
    
    def visit_region_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'template':
                return (v[0].text, v[3])
            case 'templateOptions':
                return (v[0].text, v[3][0])
            case 'reloadOnSubmit' | 'duplicateSubmissionUrl':
                return (v[0].text, v[3][0].text)
            case 'enableMetaTags' | 'enableDuplicatePageSubmissions':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_region_image(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('image', RegionImage(d))
    
    def visit_region_image_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_image_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'fileUrl' | 'accessibleDescription' | 'customAttributes':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_region_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('advanced', RegionAdvanced(d))
    
    def visit_region_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'htmlDomId' | 'regionDisplaySelector':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_region_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('source', RegionSource(d))
    
    def visit_region_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'list':
                return (v[0].text, v[3])
            case _:
                raise RuleNotImplemented()

    def visit_region_component_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('componentAppearance', RegionComponentAppearance(d))
    
    def visit_region_component_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_component_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'listTemplate' :
                return (v[0].text, v[3])
            case 'templateOptions':
                return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()

    def visit_region_settings(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else:
                raise RuleNotImplemented()
        return ('settings', RegionSettings(d))
    
    def visit_region_settings_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_csettings_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            # case 'listTemplate' :
            #     return (v[0].text, v[3])
            # case 'templateOptions':
            #     return (v[0].text, v[3][0])
            case _:
                raise RuleNotImplemented()