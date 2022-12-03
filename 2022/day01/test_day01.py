
from day01.day01 import elf_cals, max_cal

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

def test_cal():
    assert max_cal("test.txt")[-1] == 24000
    assert sum(max_cal("test.txt")[-3:]) == 45000
    