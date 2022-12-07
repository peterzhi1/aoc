

def is_unique(str: str):
    if len(str) == len(set(str)):
        return True
        
def subroutine(str: str, length: int):
    i = 0
    while i < len(str):
        if not is_unique(str[i:i+length]):
            i += 1
        else:
            return i+length
            break

def main(length):
    with open('data/signal.txt','r') as file:
        signal = file.read()
        print(subroutine(signal, length))
        
if __name__ == '__main__':
    main(4) # part 1
    main(14) # part 2
