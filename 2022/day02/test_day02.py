# Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    
# A Y
# B X
# C Z

# PART 1---------------------------------------------------------

# X for Rock, Y for Paper, and Z for Scissors. 

# A Y -> 1 2 -> (2-1) = 1 > 0 -> 2 + 6 = 8
# B X -> 2 1 -> (1-2) = -1 < 0 -> 1 + 0 = 1  
# C Z -> 3 3 -> (3-3) = 0 = 0 -> 3 + 3 = 6

# total = 8 + 1 + 6

# PART 2-----------------------------------------------------------

# X means you need to lose, Y means draw, and Z means win

# A Y -> (Y-1) = 0 -> Y = 1 -> 3 + 1 = 4
# B X -> (X-2) = -1 -> X = 1 -> 0 + 1 = 1
# C Z -> (Z-3) = 

# A Y -> A A -> 1 + 3 = 4
# B X -> B A -> 1 + 0 = 1
# C Z -> C A -> 1 + 6 = 7

# total = 4 +1 + 7 = 12

# LOGIC  ------------------------------------------------------

import pytest 

@pytest.mark.parametrize(
    ['outcome':'score'],
    ['win':6, 'lose':0, 'draw':3]
)
    
def test_strat_one():
    assert sum(game_tally()) == 15


