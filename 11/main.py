
def Part1(lines):
    #items, op, test, tr, fa = lines.split('/n')
    monkey = lines.split('\n\n')
    m,items, op, test, true, false = monkey[0].split('\n')
    ITEMS = [eval(i) for i in items.split(':')[1].replace(' ','').split(',')]
    OP = op.split('=')[-1]
    TEST = test.split(' ')[-1]
    TRUE = true.split(' ')[-1]
    FALSE = false.split(' ')[-1]

    print(m)
    print(ITEMS)
    print(OP)
    print(TEST)
    print(TRUE)
    print(FALSE)


if __name__ == "__main__":
    f = open('C:/Repos/adventofCode-2022/11/input.txt')
    lines = f.read()
    Part1(lines)
    #Part2(instructions)