from day03.day03 import priority_value, find_dup, find_badge

import pytest

test_priority_value = [
    ('a',1),
    ('z',26),
    ('A',27),
    ('Z',52),
    ('d',4),
    ('D',30),
]

test_priority_bad_inputs = [
    '',
    'ab',
    3
]

test_dup = [
    (['abc','dea'],'a'),
    (['aaa','aaa'],'a'),
    (['abc','dee'],''),
    (['abc','def'],''),
    (['a','a'],'a'),
    (['a',''],''),
]

test_badge = [
    (['123','122','133'],'1'),
    (['abc','abb','acc'],'a'),
    (['aaa','aaa','aaa'],'a'),
    (['QJRBMDMtRDCtJzBtJMfjNjhwvmNDvwjLVVgh','TPSNNPZGTjgmSmvfjL','bPlpZZbpsTlTsWprpGFCJtRtzMNdMMBBcWnJQB'],'N'),
    (['mFpDZjvmtPPGvFjmmGTzTcFRbHczHTbzQgRS','fNdqhJsNrnnVNhwNVdrdsVczQCcwCMHSTCHgHCRzHgcM','JlgnNhsqVqNqNpPlvZvDDDGlZZ'],'g'),
    (['abc','def','ghi'],''),
]

@pytest.mark.parametrize(
    'char,value',
    test_priority_value
)
def test_priority(char, value):        
    assert priority_value(char) == value


@pytest.mark.parametrize(
    'bad_input',
    test_priority_bad_inputs
)
def test_priority_bad(bad_input):
    with pytest.raises(TypeError):
        priority_value(bad_input)
        
@pytest.mark.parametrize(
    'list,unique',
    test_dup
)
def test_find_dup(list,unique):
    assert find_dup(list) == unique
    
@pytest.mark.parametrize(
    'list,unique',
    test_badge
)
def test_find_badge(list,unique):
    assert find_badge(list) == unique