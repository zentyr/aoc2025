def isAccessible(arr, r, c):
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    total = 0
    
    for d in dir:
        newR = r + d[0]
        newC = c + d[1]
        
        if newR < 0 or newR >= len(arr) or newC < 0 or newC >= len(arr[0]):
            continue

        if arr[newR][newC] == '@':
            total += 1
    
    if total < 4:
        print(total, r, c)
        return 1
    return 0

file = open('day4input.txt', 'r')

part = input("Please input 1 for part 1 or 2 for part 2: ")
arr = [line.strip() for line in file.readlines()]
res = 0

if part == '1':
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == '@':
                res += isAccessible(arr, r, c)
            
    print(res)
else:
    lastRes = res - 1
    
    while res > lastRes:
        lastRes = res
        
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if arr[r][c] == '@' and isAccessible(arr, r, c):
                    res += 1
                    row_list = list(arr[r])
                    row_list[c] = '.'
                    arr[r] = "".join(row_list)
                    
    print(res)