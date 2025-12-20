# this is pt 2 solution forgot to save pt 1
def isInvalid(id):
    i = 0
    
    while i < len(id) and id[i] == '0':
        i += 1
    
    if i == len(id):
        return True
    id = id[i:]

    l = 0
    curr = ""
    while l < len(id)//2:   
        curr += id[l]
        
        if len(curr) == 1 or len(id) % len(curr) == 0:
            if len(curr) == 1:
                currLen = len(id)
            else:
                currLen = len(id) / len(curr)
            
            if curr * int(currLen) == id:
                return True
        l += 1
    
    return False

f = open('day2input.txt', 'r')
arr = []

for line in f:
    arr.extend(line.split(','))
res = 0
#print(arr)
for ids in arr:
    if ids == '\n':
        continue
    id1, id2 = ids.split('-')
    print(id1, id2)
    
    for num in range(int(id1), int(id2)+1):
        #print(num)
        if isInvalid(str(num)):
            print(num)
            res += num

print(res)