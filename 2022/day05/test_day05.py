from day05.day05 import parse_crane, move_cargo
import pytest

# test_move_cargo = [
#     # out of bounds with no overlap
#     ([['a','b'],['c, d']],['move 1 from 1 to 2'],[['a'],['c','d','b']]),
# ]

test_parse_crane_param = [
    ('move 1 from 2 to 3',['1','2','3']),
    ('move 0 from 0 to 0',['0','0','0']),
]

# test_move_cargo_param = [
#     (
#         [['Z', 'N'], ['M', 'C', 'D'], ['P']],
#         ['move 1 from 2 to 1'],
#         [['Z', 'N', 'D'], ['M', 'C'], ['P']],
#     ),
# ]

@pytest.mark.parametrize(
    'list,expected',
    test_parse_crane_param
)
def test_parse_crane(list, expected):
    assert parse_crane(list) == expected
    
    
# @pytest.mark.parametrize(
#     'list,instruction,expected',
#     test_move_cargo_param
# )
# def test_move_cargo(list, instruction, expected):
#     assert move_cargo(list, instruction) == expected


# @pytest.mark.parametrize(
#     'stacks,crane,expected',
#     test_move_cargo
# )
# def test_move_cargo(stacks,crane, expected):
#     assert move_cargo(stacks,crane) == expected
    
