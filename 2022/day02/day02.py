# value map, doesn't work if not unique
# VALUE = {nk:nv for k,nv in [(['A','X'],1),(['B','Y'],2),(['C','Z'],3)] for nk in k}

# map letter to value
VALUE = {'A':1, 'B':2, 'C':3}
# map for strat 1, needed in case value is not uniquely mapped
MAP = {'X':'A', 'Y':'B', 'Z':'C'}
# value beats given key
WIN_GIVEN = {'A':'B', 'B':'C', 'C':'A'}

def games_list():
    games = []
    with open('data/strategy.txt','r') as file:
        for line in file:
            line = line.strip()
            games.append(line)
    return games

# part one
def strat_one():
    score=0
    tally=[]
    for game in games_list():
        # draw
        if MAP[game[2]] == game[0]:
            score = VALUE[MAP[game[2]]] + 3
        # win
        elif MAP[game[2]] == WIN_GIVEN[game[0]]:
            score = VALUE[MAP[game[2]]] + 6
        # lose
        else:
            score = VALUE[MAP[game[2]]] + 0
        tally.append(score)
    return tally

# part two
def strat_two():
    score=0
    tally=[]
    for game in games_list():
        # draw
        if game[2] == 'Y':
            score = VALUE[game[0]] + 3
        # win
        elif game[2] == 'Z':
            score = VALUE[WIN_GIVEN[game[0]]] + 6
        # lose (reverse resolution WIN_GIVEN)
        else:
            losing_hand = [k for k,v in WIN_GIVEN.items() if v==game[0]]
            score = VALUE[losing_hand[0]] + 0
        tally.append(score)
    return tally
    
def tally():
    print(f'strat 1  total: {sum(strat_one())}')
    print(f'strat 2  total: {sum(strat_two())}')
    
if __name__ == '__main__':
    tally()

    
