N = int(input())
data = []
for i in range(N):
    data.append(list(raw_input().split(' ')))
data.sort(key= lambda x : int(x[0]))    
for i,j in data:
    print(i,j)
