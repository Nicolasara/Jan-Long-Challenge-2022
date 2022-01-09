t=int(input())

def peopleInfected(d):
    if d < 11: 
        return pow(2, d)
    else:
        return pow(3, d - 10) * 1024

for _  in range(t):
    inputs = [int(item) for item in input().split()]
    n = inputs[0]
    d = inputs[1]
    if (d > 20): 
        print(n)
    else:
        print(min(n, peopleInfected(d)))