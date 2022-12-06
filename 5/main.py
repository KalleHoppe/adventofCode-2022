import re

def Part1(orders, stacks):
    result = ""
    for order in orders:
        orders = re.findall(r"(\d{1,2})", order)
        move  = int(orders[0])
        mfrom = int(orders[1])-1
        mto   = int(orders[2])-1

        for s in range(move):
            moving = stacks[mfrom].pop()
            stacks[mto].append(moving)
        
    for stack in stacks:
        result+=stack[len(stack)-1]
        #print(f"Top most crates {stack[len(stack)-1]}")
    print(result)

def Part2(orders, stacks):
    result = ""
    for order in orders:
        orders = re.findall(r"(\d{1,2})", order)
        move  = int(orders[0])
        mfrom = int(orders[1])-1
        mto   = int(orders[2])-1

        moving = []
        for s in range(move):
            moving.append(stacks[mfrom].pop())
        
        for s in range(move):
            stacks[mto].append(moving.pop())
        
    for stack in stacks:
        result += stack[len(stack)-1]
        #print(f"Top most crates {stack[len(stack)-1]}")
    print(result)

if __name__ == "__main__":
    stack1 = [
        ['N','B','D','T','V','G','Z','J',],
        ['S','R','M','D','W','P','F'],
        ['V','C','R','S','Z'],
        ['R','T','J','Z','P','H','G'],
        ['T','C','J','N','D','Z','Q','F'],
        ['N','V','P','W','G','S','F','M'],
        ['G','C','V','B','P','Q'],
        ['Z','B','P','N'],
        ['W','P','J']
    ]
    stack2 = [
        ['N','B','D','T','V','G','Z','J',],
        ['S','R','M','D','W','P','F'],
        ['V','C','R','S','Z'],
        ['R','T','J','Z','P','H','G'],
        ['T','C','J','N','D','Z','Q','F'],
        ['N','V','P','W','G','S','F','M'],
        ['G','C','V','B','P','Q'],
        ['Z','B','P','N'],
        ['W','P','J']
    ]
    f = open('C:\\Repos\\adventofCode-2022\\5\\orders.txt')
    orders = f.read().splitlines()
    # stack1 = stacks.copy()
    # stack2 = stacks.copy()
    Part1(orders,stack1)
    Part2(orders,stack2)
