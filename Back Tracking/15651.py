N,M=map(int,input().split())
check=[False]*(N+1)
data=[0]*M

def go(index,N,M):
    if index == M:
        for i in range(M):
            print(data[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        data[index] = i
        go(index+1,N,M)
go(0,N,M)