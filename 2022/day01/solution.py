# lol
# haha

#context manager
# with open('calories.txt','r') as file:
#     _DATA = file.read().split('\n')

def elf_cals():
    cal = [[]]
    with open('calories.txt','r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                cal.append([])
            else:
                cal[-1].append(int(line))
    return cal

def max_cal():
    cal_sum = []
    for elf_cal in elf_cals():
        cal_sum.append(sum(i))
    cal_sum.sort()
    print(f'max calories: {cal_sum[-1]}')
    
if __name__ == '__main__':
	max_cal()
