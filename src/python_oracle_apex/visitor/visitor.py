from parsimonious import NodeVisitor
from python_oracle_apex.objects import *
from .page import PageVisitor
from .region import RegionVisitor
from .page_item import PageItemVisitor
from .button import ButtonVisitor
from .dynamic_action import DynamicActionVisitor
from .action_c import ActionCVisitor
from .process import ProcessVisitor

from . import RuleNotImplemented

class ApxNodeVisitor(NodeVisitor, 
                     PageVisitor,
                     RegionVisitor,
                     PageItemVisitor,
                     ButtonVisitor,
                     DynamicActionVisitor,
                     ActionCVisitor,
                     ProcessVisitor
                     ):

    def visit_component(self, node, visited_children):
        return visited_children[0][0]

    def visit_component_id(self, node, visited_children):
        return node.text

    def visit_reference(self, node, visited_children):
        return node.text

    def visit_code_block(self, node, visited_children):
        if type(visited_children[0]) is str:
            return visited_children[0]

        indent_len = len(visited_children[0][1])
        lines = visited_children[0][2].split("\n")
        if indent_len == 0:
            indent_len = lines[-1].find('```')
        code = [lines[0]]
        for line in lines[1:]:
            code.append(line[indent_len:])
        return "\n".join(code)

    def visit_multiline_string(self, node, visited_children):
        return node.text

    def visit_array_of_string_like_value(self, node, visited_children):
        values = visited_children[1]
        ret = []
        for v in values:
            ret.append(v[2])

        return ret

    def visit_string_like_value(self, node, visited_children):
        t = node.text
        if t[0] == '"' and t[-1] == '"':
            return t[1:-1]
        else:
            return t

    def visit_identifier(self, node, visited_children):
        return node.text

    def visit_string(self, node, visited_children):
        return node.text[1:-1]

    def visit_boolean(self, node, visited_children):
        return node.text == 'true'

    def visit_number(self, node, visited_children):
        if '.' in node.text:
            return float(node.text)
        else:
            return int(node.text)
    
    def visit_required_ws(self, node, visited_children):
        return None

    def visit_ws(self, node, visited_children):
        return node.text

    def visit_blank_lines(self, node, visited_children):
            return None
    
    
    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node
