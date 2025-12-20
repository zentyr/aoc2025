file1 = open('day1input.txt', 'r')

part = input("Please input 1 for part 1 or 2 for part 2: ")
curr = 50
res = 0

for line in file1:
    if part == '1':
        num = int(line[1:])
        direction = line[0]
        
        if direction == 'L':
            curr = (curr - num) % 100
        else:
            curr = (curr + num) % 100
            
        if curr == 0:
            res += 1
    if part == '2':
        num = int(line[1:])
        direction = line[0]

        for _ in range(num):
            if direction == 'L':
                curr = (curr - 1) % 100
            else:
                curr = (curr + 1) % 100

            if curr == 0:
                res += 1

print(res)
