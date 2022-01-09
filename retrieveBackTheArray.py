t=int(input())
for _ in range(t):
    inputs=[int(item) for item in input().split()]
    n=inputs[0]
    x=inputs[1]

    solutions = []
    solutionsXor = 0
    for i in range(n - 1):
        solutions.append(i)
        solutionsXor = solutionsXor ^ i
    lastSolution = solutionsXor ^ x
    if lastSolution in solutions:
        if lastSolution == solutions[0]:
            solutions[1] = solutions[1] + 262144
        else:
            solutions[0] = solutions[0] + 262144
        lastSolution = lastSolution + 262144
    solutions.append(lastSolution)

    print(*solutions)