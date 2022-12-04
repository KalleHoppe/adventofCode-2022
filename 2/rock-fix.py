#Rules
#Rock 1 A
#Paper 2 B
#Scissors 3 C

#Me
#Rock 1 X
#Paper 2 Y
#Scissors 3 Z

#match Fix
#x = loose
#y = draw
# z = win

#Win 6
#Tie 3
#loss 0

data = open("C:\\Repos\\advent22\\2\\Phyton\\a\\input.txt","r")
lines = data.read().splitlines()
totalScore = 0
for line in lines:
    roundScore = 0
    elf = line[0]
    me = line[2]
    meChange = {'AX':'Z','BX':'X','CX':'Y',
                'AY':'X','BY':'Y','CY':'Z',
                'AZ':'Y','BZ':'Z','CZ':'X'}

    me = meChange.get(elf+me)

    dict_me = {'X':1,'Y':2,'Z':3}
    dict_result = {'CX':6,'BZ':6,'AY':6,
                   'AX':3,'BY':3,'CZ':3,
                   'AZ':0,'CY':0,'BX':0}
    roundScore = dict_me.get(me) + dict_result.get(elf+me)
    totalScore += roundScore
    print(f"Elf: {line[0]} - Me: {line[2]} - score: {roundScore}")

print(f"My final score was: {totalScore}")
