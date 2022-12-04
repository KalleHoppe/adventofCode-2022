def Part1(sections):
    overlapping = 0
    for sectionPair in sections:
        pair = sectionPair.split(',')
        first = FillSection(pair[0])
        second = FillSection(pair[1])
        if(first.issubset(second) | second.issubset(first)):
            #print(f"section {sectionPair}")
            overlapping+=1

    print(f"Overlaping {overlapping}")


def Part2(sections):
    overlapping = 0
    for sectionPair in sections:
        pair = sectionPair.split(',')
        first = FillSection(pair[0])
        second = FillSection(pair[1])
        intersects = first & second
        if(len(intersects) > 0):
            overlapping+=1

    print(f"Overlaping {overlapping}")

def FillSection(section):
    start = int(section.split('-')[0])
    stop = int(section.split('-')[1])
    secLenght = {start}
    if(stop-start == 0):
        return secLenght
    for x in range(start, stop+1):
        secLenght.add(x)

    #print(f"section {section} lenght {secLenght}")
    return secLenght

if __name__ == "__main__":
    with open('/workspaces/2022/4/input.txt') as f:
        lines = f.read().splitlines()
        Part1(lines)
        Part2(lines)