
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
count = 0
# for i in range(3500, 4501):
# 	if is_prime(i):
# 		count += 1

# print(count)


a = [3511, 3511, 4000, 4111]
from collections import Counter
cnt = Counter(a)
print(cnt) 


from sys import stdin
from collections import Counter

prime = [True for _ in range(8192)]
prime[0] = False
prime[1] = False
for d in range(2, 4096):
    if prime[d]:
        k = 2*d
        while k < 8192:
            prime[k] = False
            k += d

mod = 10**9+7
def f(a):
    cnt = Counter(a)
    a = list(set(a))
    n = len(a)
    dp = [[0]*8192 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for x in range(8192): 
            dp[i][x] = dp[i-1][x] * ((cnt[a[i-1]]+2)/2) + dp[i-1][x ^ a[i-1]] * ((cnt[a[i-1]]+1)/2)
            dp[i][x] %= mod
            
    res = 0
    for x in range(8192):
        if prime[x]:
            res += dp[n][x] ## at the last n 
            res %= mod
    print(dp)
    return res

# T = int(stdin.readline().strip())
# for _ in range(T):
    # n = int(stdin.readline().strip())
    # a = map(int, stdin.readline().strip().split())
n = 3
a = [3511,3511,3511]
print(f(a))



