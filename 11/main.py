
def Part1(lines):
    #items, op, test, tr, fa = lines.split('/n')
    monkey = lines.split('\n\n')
    items = monkey[1].split(':')[1].split(', ')
    op = monkey[2].split
    test = monkey[3][-1]
    
    print(monkey[0])
    print("items:" +items)
    print(op)
    print(test)


if __name__ == "__main__":
    f = open('C:/Repos/adventofCode-2022/11/input.txt')
    lines = f.read()
    Part1(lines)
    #Part2(instructions)