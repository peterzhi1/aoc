# lol
# haha
_DATA=open('calories.txt','r').read().split('\n')

def elf_cal():
    cal = [[]]
    for i in _DATA:
        if i == '':
            cal.append([])
        else:
            cal[-1].append(int(i))
    return cal

def max_cal():
    cal_sum =[]
    for i in elf_cal():
        cal_sum.append(sum(i))
    cal_sum.sort()
    print(f'max calories: {cal_sum[-1]}')
    
if __name__ == '__main__':
	max_cal()
