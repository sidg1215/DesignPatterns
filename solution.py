def solution(data, n): 
    # Your code here
    counts = {}
    for i in data:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    toReturn = []
    for i in data:
        if counts[i] <= n and counts[i] != -1:
            toReturn.append(i)
            counts[i] = -1
    return toReturn

print(solution([1,2,3,4,5], 3))