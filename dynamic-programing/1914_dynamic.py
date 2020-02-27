def dynamic(n, a, b, c):
    if(n  == 1) :
        print a, c
    else :
        dynamic(n -1 , a,c,  b)
        print a, c
        dynamic(n- 1, b, a, c)
cur = 0
i = 0


n = raw_input('')

N = int(n)

while i < N:
    cur = 2 * cur + 1
    i += 1
print(cur)
if N <= 20:
    dynamic(N, 1, 2, 3)
