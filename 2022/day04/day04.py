# combine functions, remove redundancy later
# union
def find_covered(pair):
    fs = int(pair.split(',')[0].split('-')[0])
    fe = int(pair.split(',')[0].split('-')[-1])
    ss = int(pair.split(',')[1].split('-')[0])
    se = int(pair.split(',')[1].split('-')[-1])
    if ((fs-ss)>=0 and (se-fe)>=0) or ((ss-fs)>=0 and (fe-se)>=0):
        return pair
        
# intersection
def find_overlapped(pair):
    fs = int(pair.split(',')[0].split('-')[0])
    fe = int(pair.split(',')[0].split('-')[-1])
    ss = int(pair.split(',')[1].split('-')[0])
    se = int(pair.split(',')[1].split('-')[-1])
    if not (fs > se or fe < ss):
        return pair
       
def tally():
    pairs = []
    covered = []
    overlapped = []
    count = 0
    with open('data/cleanup.txt') as file:
        for line in file:
            line = line.strip()
            pairs.append(line)
        for pair in pairs:
            covered.append(find_covered(pair))
            overlapped.append(find_overlapped(pair))
    covered = [x for x in covered if x]
    overlapped = [x for x in overlapped if x]
    # print(f'covered: {covered}')
    print(f'count covered {len(covered)}')
    # print(f'overlapped: {overlapped}')
    print(f'count overlapped {len(overlapped)}')


if __name__ == '__main__':
    tally()