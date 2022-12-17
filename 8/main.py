from math import prod

def Part1(trees):
    answer = 0
    for rownum, row in enumerate(trees):
        for colnum, tree in enumerate(row):
            answer += (
                all(trees[rownum][j] < tree for j in range(0, colnum))
                or all(trees[rownum][j] < tree for j in range(colnum + 1, len(row)))
                or all(trees[i][colnum] < tree for i in range(0, rownum))
                or all(trees[i][colnum] < tree for i in range(rownum + 1, len(trees)))
            )
    return print(f"The answer is: {answer}")


def Part2(trees):
    ans = []

    for rownum, row in enumerate(trees):
        for colnum, tree in enumerate(row):
            treeSight = [0, 0, 0, 0]
            
            for j in range(colnum - 1, -1, -1):
                treeSight[0] += 1
                if trees[rownum][j] >= tree:
                    break
            
            for i in range(rownum - 1, -1, -1):
                treeSight[1] += 1
                if trees[i][colnum] >= tree:
                    break
            
            for j in range(colnum + 1, len(row)):
                treeSight[2] += 1
                if trees[rownum][j] >= tree:
                    break

            for i in range(rownum + 1, len(trees)):
                treeSight[3] += 1
                if trees[i][colnum] >= tree:
                    break
            ans.append(treeSight)

    result = max(prod(x) for x in ans)
    print(f"The answer is: {result}")

if __name__ == "__main__":
    f = open('/workspaces/adventofCode-2022/8/input.txt')
    trees = f.read().splitlines()
    Part1(trees)
    Part2(trees)