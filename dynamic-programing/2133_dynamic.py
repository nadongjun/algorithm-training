d = [None] * 1001

def dynamic(n):
    if(n % 2 != 0) :
        return 0
    else :
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[2] = 3
        for i in range(4, n + 1):
            dp[i] = dp[i - 2] * 3
            for j in range(i - 4, -1, -2):
                dp[i] += dp[j] * 2
        return dp[n]

n = raw_input('')

N = int(n)
print(dynamic(N))

#Python 2.7.10
