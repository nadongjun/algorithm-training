d = [0] * 2

d = map(int, raw_input().split())
coin = [0] * d[0]

count = 0

for i in range(d[0]):
    coin[i] = int(raw_input(''))    

for j in range(d[0] - 1 ,0,-1):

        count = count + d[1] / coin[j]
        d[1] = d[1] - (d[1] / coin[j]) * coin[j]
 
print(count)

#Python 2.7.10
