# part 1 - find duplicates between compartments
def find_dup(list):
    dup = ''
    for char in list[0]:
        if char in list[1]:
            dup = char
    return dup   

# part 2 - find shared unique badges between three elves
def find_badge(list):
    badge = ''
    for char in list[0]:
        if (char in list[1] and char in list[2]):
            badge = char
    return badge   
    
# determine priority value of each dup char
def priority_value(char):
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return (ord(char)-ord('A')+27)
    elif ord(char) >= ord('a') and ord(char) <= ord('z'):
        return (ord(char)-ord('a')+1)
    else:
        return 0    

# tally up the scores
def tally():
    dups = []
    dups_tally = []
    badges = []
    badges_tally = [] 
    rucksacks = []
    elf_groups = []
    elf_index = 0
    with open('data/rucksack.txt','r') as file:
        items = file.read().split('\n')
        for item in items:
            rucksacks.append([item[:int(len(item)/2)],item[int(len(item)/2):]])
        while elf_index <= len(items)-3: 
            elf_groups.append(items[elf_index:elf_index+3])
            elf_index += 3
    for rucksack in rucksacks:
        dups.append(find_dup(rucksack))
        dups_tally.append(priority_value(find_dup(rucksack)))
    for group in elf_groups:
        badges.append(find_badge(group))
        badges_tally.append(priority_value(find_badge(group)))
    # print(f'duplicates: {dups}')
    # print(f'duplicates tally: {dups_tally}')
    print(f'duplicates sum: {sum(dups_tally)}')
    # print(f'badges: {badges}')
    # print(f'badges tally: {badges_tally}')
    print(f'badges sum: {sum(badges_tally)}')

if __name__ == '__main__':
    tally()
    





