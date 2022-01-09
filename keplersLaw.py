t=int(input())
for _ in range(t):
    inputs = [int(item) for item in input().split()]
    ratioOne = pow(inputs[0], 2) / pow(inputs[2], 3)
    ratioTwo = pow(inputs[1], 2) / pow(inputs[3], 3)
    if (ratioTwo == ratioOne):
        print("Yes")
    else:
        print("No")