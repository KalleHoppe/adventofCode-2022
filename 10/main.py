

def Part1(instructions):
    stren = 0
    cycle = 0
    nxt = 20
    register = 1

    for instruction in instructions:
        command = instruction.split(' ')[0]
        if command == 'addx':
            cycle += 2
        else:
            cycle += 1

        if cycle >= nxt:
            stren += nxt * register
            nxt += 40
        
        if command == 'addx':
            register += int(instruction.split(' ')[1])

    print(f'Total signal strength: {stren}')


def Part2(instructions):
    row = []
    register = 1

    for instruction in instructions:
        command = instruction.split(' ')[0]
        if command == 'noop':
            row.append(register)
        else:
            row.extend([register, register])
            register += int(instruction.split(' ')[1])

    for i, val in enumerate(row):
        pos = i % 40
        #Sprite position #val#
        if pos in [val - 1, val, val + 1]:
            print("#", end="")
        else:
            print(".", end="")

        if pos == 39:
            print()

if __name__ == "__main__":
    f = open('/workspaces/adventofCode-2022/10/input.txt')
    instructions = f.read().splitlines()
    Part1(instructions)
    Part2(instructions)