from python_oracle_apex import *


def test_computation_c_0(apex_parser):
    c: ComputationA = apex_parser.parse(
"""computation A (
    )
""")

    assert isinstance(c, ComputationA)
