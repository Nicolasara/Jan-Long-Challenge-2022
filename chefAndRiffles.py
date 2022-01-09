t=int(input())

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y) // gcd(x,y)
   return lcm

def riffle(permutations, n, k):
    positions = []
    for i in range(n):
        positions.append(i + 1)

    for permutation in permutations:
        for i in range(len(permutation)):
            positions[permutation[(i + k) % len(permutation)]] = permutation[i] + 1
    return positions

def backwardsRiffe(positions, n):
    newPositions = []
    positionsFirstHalf = positions[0:n//2]
    positionsSecondHalf = positions[n//2:]
    for i in range(n//2):
        newPositions.append(positionsFirstHalf[i])
        newPositions.append(positionsSecondHalf[i])       
    return newPositions
    
def singleRiffle(currentPositions, n):
    if currentPositions % 2:
        return n // 2 + (currentPositions - 1) // 2
    else:
        return currentPositions // 2

def findOrder(permutations):
    if len(permutations) == 0:
        return 1
    order = len(permutations[0])
    for permutation in permutations:
        order = lcm(order, len(permutation))
    return order
    
def findPermutations(n):
    permutations = []
    positionsNotSeen = set()
    for i in range(1, n - 1):
        positionsNotSeen.add(i)
    count = 0
    while count != n - 2:
        permutation = []
        startingPosition = positionsNotSeen.pop()
        currentPosition = startingPosition
        currentPosition = singleRiffle(currentPosition, n)
        permutation.append(currentPosition)
        count += 1
        while startingPosition != currentPosition:
            positionsNotSeen.remove(currentPosition)
            currentPosition = singleRiffle(currentPosition, n)
            permutation.append(currentPosition)
            count += 1
        permutations.append(permutation)
    return permutations

for _ in range(t):
    inputs=[int(item) for item in input().split()]
    n=inputs[0]
    k=inputs[1]
    permutations = findPermutations(n)
    order = findOrder(permutations)
    riffleAmount = k % order
    print(*riffle(permutations, n, k))