import re

def Part1(dirs):
    structure = {'/':0}
    paths = ['/']
    for line in dirs:
        # Don't need to consicer root, dir ,nor ls
        # we only care about cd and ..
        #cd into dir
        cdToDir = re.match('\$ cd (\w+)', line)
        cdBack = re.match('\$ cd \.\.', line)
        if cdToDir is not None:
            if paths:
                paths.append(f'{paths[-1]}{cdToDir[1]}')
            else:
                paths.append(cdToDir[1])
        elif cdBack is not None:
            paths = paths[:-1]
        elif line[0].isdigit():
            filesize = int(line.split(' ')[0])
            for path in paths:
                if path in structure:
                    structure[path] += filesize
                else:
                    structure[path] = filesize
    
    #Part 1 result            
    resutlt = sum([item for item in structure.values() if item <= 100000])

    #Part 2
    freeSpace = 70000000 - int(structure['/'])
    minFolder = min(folderSize for folderSize in structure.values() if folderSize >= 30000000 - freeSpace)

    print(f'Sum of all dirs lower than 100000: {resutlt}')
    print(f'Min folder: {minFolder}')

if __name__ == "__main__":
    with open('/workspaces/adventofCode-2022/7/input.txt') as f:
        dirs = f.read().splitlines()
        Part1(dirs)