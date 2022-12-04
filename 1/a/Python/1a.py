input = open("C:\\Repos\\advent22\\1\\a\\Python\\input.txt","r")
lines = input.readlines()

mostCals = 0
currSum = 0
for line in lines:
    l = line.rstrip('\n')
    if(l.isnumeric()):
        currSum += int(l)
    else:
        if(currSum > mostCals):
            mostCals = currSum
            print(f"new leader with {mostCals}")
        currSum = 0;        

print(f"And the efl with mots cals had {mostCals}")