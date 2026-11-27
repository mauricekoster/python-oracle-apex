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
                if isinstance(item[1], ApexGroup):
                    region.add_group(item[0], item[1])
                else:
                    region.add_property(item[0], item[1])
            elif isinstance(item, ApexObject):
                region.add_child(item)
            elif item is None:
                # blanklines
                continue
            else: # pragma: no cover
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

    def visit_region_child_component(self, node, visited_children):
        return visited_children[0]

    def visit_region_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('layout', RegionLayout(d) )
    
    def visit_region_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'sequence' | 'slot' | 'parentRegion' | 'startNewRow':
                return (v[0].text, v[3])
            # case 'reloadOnSubmit' | 'duplicateSubmissionUrl':
            #     return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('appearance', RegionAppearance(d))
    
    def visit_region_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'template' | 'templateOptions' | 'cssClasses' | 'icon':
                return (v[0].text, v[3])
            case 'renderComponents':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_image(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('image', RegionImage(d))
    
    def visit_region_image_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_image_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'fileUrl' | 'accessibleDescription' | 'customAttributes':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented()

    def visit_region_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('advanced', RegionAdvanced(d))
    
    def visit_region_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'htmlDomId' | 'regionDisplaySelector' | 'savedReportMappingIdentifier':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_source(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('source', RegionSource(d))
    
    def visit_region_source_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_source_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'list' | 'breadcrumb' | 'filteredRegion' | 'type' | 'sqlQuery' | 'plsqlFunctionBody' | 'htmlCode':
                return (v[0].text, v[3])
            case 'location':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_component_appearance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('componentAppearance', RegionComponentAppearance(d))
    
    def visit_region_component_appearance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_component_appearance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'listTemplate' | 'breadcrumbTemplate' | 'display' | 'templateOptions' | 'cssClasses' | 'customAttributes' | 'showNullValuesAs' | 'selectFirstRow' | 'fixedRowHeight':
                return (v[0].text, v[3])
            case 'layout' | 'gridColumns' | 'templateType':
                return (v[0].text, v[3][0].text)
            case 'template':
                if type(v[3][0]) is str:
                    return (v[0].text, v[3][0])
                else:
                    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_settings(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('settings', RegionSettings(d))
    
    def visit_region_settings_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_settings_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'title' | 'description' | 'miscellaneous' | \
                    'displayAvatar' | 'displayBadge' | 'overline' |\
                    'compactNosThreshold' | 'currentFacetsSelector' | 'displayChartForTopNValues':
                return (v[0].text, v[3])
            case 'displayColumn' | 'startDateColumn' | 'additionalCalendarViews' | 'maxEventsDay':
                return (v[0].text, v[3])
            case 'timeAxisType' | 'zoomAndScroll' | 'outputAs' | 'export':
                return (v[0].text, v[3][0].text)
            case 'showCurrentFacets' :
                return (v[0].text, v[3].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_plugin_avatar(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('plugin-avatar', RegionPluginAvatar(d))
    
    def visit_region_plugin_avatar_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_plugin_avatar_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            case 'icon' :
                return (v[0].text, v[3])
            # case 'templateOptions':
            #     return (v[0].text, v[3][0])
            # case 'showCurrentFacets':
            #     return (v[0].text, v[3].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_plugin_badge(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('plugin-badge', RegionPluginBadge(d))
    
    def visit_region_plugin_badge_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_plugin_badge_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'label' | 'value' | 'state':
                return (v[0].text, v[3])
            case 'columnWidth':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_pagination(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('pagination', RegionPagination(d))
    
    def visit_region_pagination_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_pagination_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'entitiesPerPage' | 'partialPageRefresh' | 'showTotalCount' | 'maxRowsToDisplay' | 'cardsPerPage' | 'initialEntitiesCount':
                return (v[0].text, v[3])
            case 'type':
                if type(v[3]) is list:
                    return (v[0].text, v[3][0].text)
                else:
                    return (v[0].text, v[3])
            case 'displayPosition':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_accessibility(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('accessibility', RegionAccessibility(d))
    
    def visit_region_accessibility_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_accessibility_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'useLandmark' | 'landmarkLabel':
                return (v[0].text, v[3])
            case 'landmarkType':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented()             

    def visit_region_report_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('reportLayout', RegionReportLayout(d))
    
    def visit_region_report_layout_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_report_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'numberOfRows' | 'item':
                return (v[0].text, v[3])
            case 'numberOfRowsType':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_performance(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('performance', RegionPerformance(d))
    
    def visit_region_performance_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_performance_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'lazyLoading' | 'maxRowsToProcess':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")            

    def visit_region_messages(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('messages', RegionMessages(d))
    
    def visit_region_messages_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_messages_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'whenNoDataFound' | 'whenMoreDataFound' | 'noDataFoundIcon':
                return (v[0].text, v[3])
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_component_advanced(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('componentAdvanced', RegionComponentAdvanced(d))
    
    def visit_region_component_advanced_property_line(self, node, visited_children):
        return visited_children[1]

    def visit_region_component_advanced_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'stripHtml' | 'customSvgStyles' | 'oracleTextIndexColumn' | 'emailFromAddress' | 'initJavaScriptFunction' | 'regionAlias' | 'reportIdItem' | 'maxRowsPerPageInSelector':
                return (v[0].text, v[3])
            case 'sortNulls':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")            

    def visit_region_chart(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('chart', RegionChart(d))
    
    def visit_region_chart_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_chart_property(self, node, visited_children):
        v = visited_children
        match v[0].text:
            #case '':
            #    return (v[0].text, v[3])
            case 'type':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_title(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('title', RegionTitle(d))
    
    def visit_region_title_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_title_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'title' | 'advancedFormatting' | 'column' | 'htmlExpression' | 'cssClasses':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_chart_layout(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('chartLayout', RegionChartLayout(d))
    
    def visit_region_chart_layout_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_chart_layout_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'maxWidth' | 'height':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")            

    def visit_region_legend(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('legend', RegionLegend(d))
    
    def visit_region_legend_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_legend_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'show' | 'title' | 'selector' | 'cssClasses' | 'fontColor':
                return (v[0].text, v[3])
            case 'position' | 'hideAndShowBehavior' | 'fontFamily' | 'fontStyle' | 'fontSize':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_server_side_condition(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('serverSideCondition', RegionServerSideCondition(d))
    
    def visit_region_server_side_condition_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_server_side_condition_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'type' | 'sqlExpression':
                return (v[0].text, v[3])
            case 'language':
                return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_entity_title(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('entityTitle', RegionEntityTitle(d))
    
    def visit_region_entity_title_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_entity_title_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'singular' | 'plural':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_gen_ai(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('genAI', RegionGenAI(d))
    
    def visit_region_gen_ai_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_gen_ai_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'naturalLanguageSupport':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_actions_menu(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('actionsMenu', RegionActionsMenu(d))
    
    def visit_region_actions_menu_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_actions_menu_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'savePublicReport':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_download(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('download', RegionDownload(d))
    
    def visit_region_download_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_download_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'formats':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_page(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('page', RegionPage(d))
    
    def visit_region_page_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_page_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'borderWidth' | 'borderColor':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_page_header(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('pageHeader', RegionPageHeader(d))
    
    def visit_region_page_header_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_page_header_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'pageHeaderText':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")

    def visit_region_security(self, node, visited_children):
        parts = visited_children[5]
        d = {}
        for item in parts:
            if type(item) is tuple:
                d[item[0]] = item[1]
            else: # pragma: no cover
                raise RuleNotImplemented()
        return ('security', RegionSecurity(d))
    
    def visit_region_security_property_line(self, node, visited_children):
        return visited_children[1]
    
    def visit_region_security_property(self, node, visited_children):
        v = visited_children[0]
        match v[0].text:
            case 'authorizationScheme' | 'escapeSpecialChars':
                return (v[0].text, v[3])
            #case '':
            #    return (v[0].text, v[3][0].text)
            case _: # pragma: no cover
                raise RuleNotImplemented(f"rule: {node.expr_name}   text: '{node.text}'")