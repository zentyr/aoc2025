def max_subsequence_number(s, k):
    stack = []
    to_drop = len(s) - k

    for ch in s:
        while stack and to_drop > 0 and stack[-1] < ch:
            stack.pop()
            to_drop -= 1
        stack.append(ch)

    return int("".join(stack[:k]))

file1 = open('day3input.txt', 'r')

part = input("Please input 1 for part 1 or 2 for part 2: ")

if part == '1':
    finalAnswer = 0

    for line in file1:
        line = line.strip()
        l, r = 0, 1
        currMax = '0'
        res = 0
        
        while r < len(line):
            if r == len(line)-1:
                if int(line[r]) > int(currMax):
                    currMax = line[r]
                res = int(line[l] + currMax)
                
            if int(line[r]) > int(line[l]):
                l = r
                currMax = '0'
            elif int(line[r]) > int(currMax):
                currMax = line[r]
            
            r += 1
        # print(res)
        finalAnswer += res
        
    print(finalAnswer)
    
else:
    finalAnswer = 0

    for line in file1:
        line = line.strip()
        best = max_subsequence_number(line, 12)
        print(best)
        finalAnswer += best

    print(finalAnswer)