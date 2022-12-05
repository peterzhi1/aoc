from day04.day04 import find_covered, find_overlapped
import pytest 

test_covered = [
    # out of bounds with no overlap
    ('1-3,4-6',None),
    # out of bounds with some overlap
    ('1-3,2-6',None),
    # out of bounds with no overlap fr
    ('4-6,1-3',None),
    # out of bounds with some overlap rr
    ('2-6,1-3',None),
    # out of bounds single
    ('1,2',None),
    # covers fr
    ('1-4,2-3','1-4,2-3'),
    # covers rr
    ('2-3,1-4','2-3,1-4'),
    # covers fr single
    ('1-4,2','1-4,2'),
    # covers rr single
    ('2,1-4','2,1-4'),
    # covers all single
    ('1,1','1,1'),
    # out of bounds with no overlap
    ('11-33,44-66',None),
    # out of bounds with some overlap
    ('11-33,22-66',None),
    # out of bounds with no overlap fr
    ('44-66,11-33',None),
    # out of bounds with some overlap rr
    ('22-66,11-33',None),
    # out of bounds double
    ('11,22',None),
    # covers fr
    ('11-44,22-33','11-44,22-33'),
    # covers rr
    ('22-33,11-44','22-33,11-44'),
    # covers fr single
    ('11-44,22','11-44,22'),
    # covers rr single
    ('22,11-44','22,11-44'),
    # covers all double
    ('11,11','11,11'),
]

# change some overlap to successful
test_overlapped = [
    # out of bounds with no overlap
    ('1-3,4-6',None),
    # out of bounds with some overlap
    ('1-3,2-6','1-3,2-6'),
    # out of bounds with no overlap fr
    ('4-6,1-3',None),
    # out of bounds with some overlap rr
    ('2-6,1-3','2-6,1-3'),
    # out of bounds single
    ('1,2',None),
    # covers fr
    ('1-4,2-3','1-4,2-3'),
    # covers rr
    ('2-3,1-4','2-3,1-4'),
    # covers fr single
    ('1-4,2','1-4,2'),
    # covers rr single
    ('2,1-4','2,1-4'),
    # covers all single
    ('1,1','1,1'),
    # out of bounds with no overlap
    ('11-33,44-66',None),
    # out of bounds with some overlap
    ('11-33,22-66','11-33,22-66'),
    # out of bounds with no overlap fr
    ('44-66,11-33',None),
    # out of bounds with some overlap rr
    ('22-66,11-33','22-66,11-33'),
    # out of bounds double
    ('11,22',None),
    # covers fr
    ('11-44,22-33','11-44,22-33'),
    # covers rr
    ('22-33,11-44','22-33,11-44'),
    # covers fr single
    ('11-44,22','11-44,22'),
    # covers rr single
    ('22,11-44','22,11-44'),
    # covers all double
    ('11,11','11,11'),
]


@pytest.mark.parametrize(
    'str,expected',
    test_covered
)
def test_find_covered(str,expected):
    assert find_covered(str) == expected
    
@pytest.mark.parametrize(
    'str,expected',
    test_overlapped
)
def test_find_overlapped(str,expected):
    assert find_overlapped(str) == expected