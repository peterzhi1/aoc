#context manager
# with open('calories.txt','r') as file:
#     _DATA = file.read().split('\n')


def elf_cals(input_file):
    cal = [[]]
    with open(input_file,'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                cal.append([])
            else:
                cal[-1].append(int(line))
    return cal

def max_cal(input_file):
    cal_sum = []
    for elf_cal in elf_cals(input_file):
        cal_sum.append(sum(elf_cal))
    cal_sum.sort()
    return cal_sum
    
def main():
    # print(cal_sum)
    print(f'p1 max calories: {max_cal("calories.txt")[-1]}')
    print(f'p2 sum of top three: {sum(max_cal("calories.txt")[-3:])}')
    # print(f'top three: {max_cal("calories.txt")[-3:]}')

if __name__ == '__main__':
	main()
