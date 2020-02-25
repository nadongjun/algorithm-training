

d = [0] * 4

d = map(int, raw_input().split())
c = 1
s = 1
count = 0

for i in range(1, d[2]):
   
    if((d[0] * i) + d[1] * (d[2]- i) == d[3] and i >= 1 and (d[2] - i) >= 1) :
        s = i
        c = d[2] - i
        count = count + 1

if(count != 1): 
    print("-1")
else :
    print('%d %d' %(s,c))
  

