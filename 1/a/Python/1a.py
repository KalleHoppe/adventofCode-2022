data = open("/workspaces/adventofCode-2022/1/a/Pythonz/input.txt","r")
lines = data.readlines()

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