import math

def Part1(lines, rounds):
    MONKEY = []
    OP = []
    DIV = []
    TRUE = []
    FALSE = []
    #items, op, test, tr, fa = lines.split('/n')
    for monkey in lines.split('\n\n'):
        id_, items, op, test, true, false = monkey.split('\n')
        MONKEY.append([int(i) for i in items.split(':')[1].split(',')])
        OP.append(lambda old, op=op: eval(op.split('=')[-1]))
        DIV.append(int(test.split()[-1]))
        TRUE.append(int(true.split()[-1]))
        FALSE.append(int(false.split()[-1]))
    #print(ITEMS)
        #print(OP[-1](2))

    #Least common multiple
    lcm = 1
    if rounds > 20:
        for x in DIV:
            lcm *= (lcm*x)#//math.gcd(lcm,x)


    C = [0 for _ in range(len(MONKEY))]
    for _ in range(rounds):
        for i in range(len(MONKEY)):
        #for i in eval(MONKEY):
            for item in MONKEY[i]:
                C[i] += 1
                item = OP[i](item)
                if rounds > 20:
                    item %= lcm
                else:
                    item = (item // 3)
                if item % DIV[i] == 0:
                    MONKEY[TRUE[i]].append(item)
                else:
                    MONKEY[FALSE[i]].append(item)
                
            MONKEY[i] = []
    srtd = sorted(C)
    print(srtd[-1] * srtd[-2])

if __name__ == "__main__":
    f = open('/workspaces/adventofCode-2022/11/input.txt')
    lines = f.read().strip()
    Part1(lines,20)
    Part1(lines,10000)
    #Part2(instructions)