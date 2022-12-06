from day06.day06 import is_unique, subroutine
import pytest 

test_is_unique_params = [
    ('', True),
    ('a', True),
    ('ab', True),
    ('ab3', True),
    ('abcd',True),
    ('ab', True),
    ('a1', True),
    ('aa', None),
    ('aba', None),
    ('abbb', None)
]

test_subroutine_packets_messages = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb',4,7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz',4,5),
    ('nppdvjthqldpwncqszvftbrmjlhg',4,6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',4,10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',4,11),   
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb',14,19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz',14,23),
    ('nppdvjthqldpwncqszvftbrmjlhg',14,23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',14,29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',14,26)     
]


@pytest.mark.parametrize(
    'str,boolean',
    test_is_unique_params
)
def test_is_unique(str,boolean):
    assert is_unique(str) == boolean
    
@pytest.mark.parametrize(
    'str,length,int',
    test_subroutine_packets_messages
)
def test_subroutine(str,length,int):
    assert subroutine(str,length) == int