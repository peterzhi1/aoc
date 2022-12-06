# parse instructions into list
def parse_crane(instruction):
    return [x for x in instruction.split(' ') if not x in ['move','from','to']]

# part 1 logic for moving cargo between stacks
def move_cargo(cargo,cranes):
    for crane in cranes:
        move = cargo[int(crane[1])-1][-int(crane[0]):]
        cargo[int(crane[2])-1] = cargo[int(crane[2])-1] + list(reversed(move))
        cargo[int(crane[1])-1] = cargo[int(crane[1])-1][:-int(crane[0])]
    return cargo
    
# part 2 logic for moving cargo between stacks
def move_cargo_9001(cargo,cranes):
    for crane in cranes:
        move = cargo[int(crane[1])-1][-int(crane[0]):]
        cargo[int(crane[2])-1] = cargo[int(crane[2])-1] + (move)
        cargo[int(crane[1])-1] = cargo[int(crane[1])-1][:-int(crane[0])]
    return cargo
    
def rearrange(type):
    text = []
    with open('data/cargo.txt','r') as file:
        for line in file:
            line = line.replace('\n','')
            text.append(line)
        # set up crane instructions
        cranes = [] 
        for n in text[text.index('')+1:]:
            cranes.append(parse_crane(n))
        # set up cargo
        cargo = [[]]
        index = 1
        while index <= len(text[0]):
            for t in list(reversed(text[:text.index('')-1:])):
                cargo[-1].append(t[index]) 
            index += 4
            cargo.append([])
        cargo = cargo[:-1]
        # get rid of empty stacks
        for i in range(0,len(cargo)):
            cargo[i] = [n for n in cargo[i] if n != ' ']
        # stack cargo
        if type == '9001':
            move_cargo_9001(cargo,cranes)
        else:  
            move_cargo(cargo, cranes)
    return cargo

def main():
    part1 = ''
    for c in rearrange('standard'):
        part1 = part1 + c[-1]
    print(part1)
    part2 = ''
    for c in rearrange('9001'):
        part2 = part2 + c[-1]
    print(part2)

if __name__ == '__main__':
    main()