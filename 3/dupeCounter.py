import math
from collections import Counter

pInput = open("/workspaces/adventofCode-2022/3/input.txt")
lines = pInput.read().splitlines()
duplicates = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def findDuplicate(line):
    #Split string
    middle = math.ceil(len(line)/2)
    left = line[:middle]
    right = line[middle:len(line)]

    #Compare strings
    duplicate = []
    for char in left:
        for c in right:
            if char == c :
                duplicate.append(c)
    print(f"{duplicate} - {left} : {right}")
    return duplicate[0]

if __name__ == "__main__":
    totalCount = 0
    for line in lines:
        duplicates = findDuplicate(line)
        for dup in duplicates:
            totalCount += letters.index(dup)+1

    print(f"Sum of all is: {totalCount}")
