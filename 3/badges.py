pInput = open("/workspaces/adventofCode-2022/3/input.txt")
lines = pInput.read().splitlines()
duplicates = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def findDuplicate(left, mid, right):
    duplicate = []
    for leftChar in left:
        for midChar in mid:
            if(leftChar == midChar):
                #Two have same check third also
                for rightChar in right:
                    if(rightChar == midChar):
                        duplicate.append(midChar)
    return duplicate[0]

if __name__ == "__main__":
    totalCount = 0
    lineLenght = len(lines)
    for x in range(0,lineLenght,3):
        duplicates = findDuplicate(lines[x],lines[x+1],lines[x+2])
        val = 0
        for dup in duplicates:
            val = letters.index(dup)+1
            totalCount += val
            print(f"{dup}-{val} -- {lines[x]} - {lines[x+1]} - {lines[x+2]}")

    print(f"Sum of all is: {totalCount}")
