N,M=map(int,input().split())
check=[False]*(N+1)
data=[0]*M

def Suyeol(index,start,N,M):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(start,N+1):
        if check[i] == True:
            continue
        check[i]=True
        data[index]=i
        Suyeol(index+1,i+1,N,M)
        check[i]=False
Suyeol(0,1,N,M)