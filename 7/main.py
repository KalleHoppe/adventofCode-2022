from collections import defaultdict
from pathlib import Path

def Part1(files):
    dirs = {}
    depth = 0
    count = 0
    for path in files:
        if path.startswith("$ cd /"):
            depth = 0
        elif path.startswith("$ cd .."):
            depth -= 1
        elif path.startswith("$ cd "):
            dirs.append(path.split(' ')[2])
            depth += 1
        elif path[0].isdigit(): 
            dirs[-1] += int(path.split(' ')[0])
    
    count = for d in dirs 



if __name__ == "__main__":
    f = open('/workspaces/adventofCode-2022/7/input.txt')
    files = f.read().splitlines()
    Part1(files)
    #Part2(trees)