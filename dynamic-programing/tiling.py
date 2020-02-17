d = [None] * 1001

def dynamic(n):

    if(n == 1): 
        return 1
    if(n == 2): 
        return 2
    if(d[n] !=  None): 
        return d[n]
    d[n] = (dynamic(n - 1) + dynamic(n - 2)) % 10007
    return d[n] 


n = raw_input('')

N = int(n)
print(dynamic(N))

#Python 2.7.10
