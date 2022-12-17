
def moveT(H, T):  
    diffR = (H[0] - T[0])
    diffC = (H[1] - T[1])
    if abs(diffR) <= 1 and abs(diffC) <=1:
        pass
    elif abs(diffR)>=2 and abs(diffC)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(diffR)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(diffC)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T

def Part1(lines, part):
    H = (0,0)
    T = [(0,0) for _ in range(9)]
    DR = {'L': 0, 'U':-1, 'R':0, 'D':1}
    DC = {'L': -1, 'U':0, 'R':1, 'D':0}
    TPOS = set()

    for line in lines:
        direction, steps = line.split()
        steps = int(steps)
        for _ in range(steps):
            if part == 1:
                TPOS.add(T[1])
            else:
                TPOS.add(T[8])
            H = (H[0] + DR[direction], H[1] + DC[direction])
            T[0] = moveT(H, T[0])
            for i in range(1, 9):
                T[i] = moveT(T[i-1], T[i])
            TPOS.add(T[8])
    print(len(TPOS))


    
# def Part1(steps):
#     path = set([(0,0)])
    
#     hx = 0
#     hy = 0
#     tx = 0
#     ty = 0
#     for step in steps:
#         direction = step[0]
#         times = int(step[2])
#         for s in range(times):
#             diff_x = hx-tx
#             diff_y = hy-ty

#             if direction == 'R':
#                 hx += 1
#                 if abs(hx-tx) > 1:
#                     tx = hx-1
#                     if hy != ty:
#                         ty=hy

#             elif direction == 'L':
#                 hx += -1
#                 if abs(hx-tx) > 1:
#                     tx = hx+1
#                     if hy != ty:
#                         ty=hy

#             elif direction == 'U':
#                 hy += 1
#                 if abs(hy-ty) > 1:
#                     ty = hy-1
#                     if hx != tx:
#                         tx=hx
#             elif direction == 'D':
#                 hy += -1
#                 if abs(hy-ty) > 1:
#                     ty = hy+1
#                     if hx != tx:
#                         tx=hx


#             path.add(tuple([tx,ty]))
#         #print(f"Paths {path}")
#     print(f'Steps taken: {len(path)}')


if __name__ == "__main__":
    f = open('/workspaces/adventofCode-2022/9/input.txt')
    lines = f.read().splitlines()
    Part1(lines,1)
    Part1(lines,2)