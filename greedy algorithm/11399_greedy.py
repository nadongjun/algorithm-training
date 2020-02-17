count = int(raw_input(''))
d = [None] * count

d = map(int, raw_input().split())

#for i in range(count):
 #   d = map(int, raw_input().split())
d.sort()
#print(d)
sum = 0
total = 0
for j in range(count):
    
    sum = sum + d[j]
    total = sum + total
    #print(sum)
    

print(total)
#Python 2.7.10
