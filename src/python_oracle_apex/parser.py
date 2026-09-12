from parsimonious import Grammar
from python_oracle_apex.objects import *
from importlib import resources as impresources
from pathlib import Path


import python_oracle_apex
from .visitor import ApxNodeVisitor


class ApexParser:
    def __init__(self, apex_version : str ="26.1"):
        inp_file = impresources.files(python_oracle_apex) / f'apexlang-{apex_version}.peg'
        with inp_file.open("rt") as f:
            template = f.read()
    
        self.grammar = Grammar(template)
        self.visitor = ApxNodeVisitor()

    def parse(self, data) -> ApexObject:
        nodes = self.grammar.parse(data)
        output = self.visitor.visit(nodes)
        return output

    def parse_file(self, apex_file: str | Path):
        if type(apex_file) is str:
            fn = Path(apex_file)
        else:
            fn = apex_file
        with fn.open('r') as f:
            data = f.read()

        return self.parse(data)


def parse_apex_file(apex_file: str | Path, apex_version : str = "26.1") -> ApexObject:
    return ApexParser(apex_version).parse_file(apex_file)

def parse_apex(data: str, apex_version : str = "26.1") -> ApexObject:
    return ApexParser(apex_version).parse(data)

