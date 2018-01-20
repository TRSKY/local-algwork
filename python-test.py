
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
# print(f(a))



###review the solution below to understand what is going on. 

n, k = map(int, input().split())
if k > n // 2:
    k = n - k

# sort the array, so that when processing ith number in a, we know a[i] is
# larger than or equal to previously processed numbers, so calculating abs
# is easier
a = sorted(map(int, input().split()))

# dp[i][j] is the value when ith number in a has already processed, and j of
# those numbers assigned to li, initialize all value to maximum number
dp = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]

# When i==0, j==0, no number assigned, the value is zero
dp[0][0] = 0


for i in range(0, n):  # iter through a
    # iter through the possiblities of sizes in li when a[i] needs to be
    # assigned
    for j in range(0, i + 1):

        # We ignore the cases when the number of li or lu larger than required
        if j > k or i - j > n - k:
            continue

        # There are two possiblities: (1)assign a[i] to li (2) or to lu

        # Possiblity (1) assign to li:
        # If a[i] would be assigned to li:
        #       all the numbers in lu needs to be substracted from a[i],
        #       so we add (i -j)* a[i] to d[i][j].
        #       Note: substraction of all lu has been done in prevous steps
        #       (see below, 3 lines later)
        #       (i-j) is the current number in lu.
        #
        #       a[i] WILL be substracted from all future a[x] assigned to lu,
        #       so we substract (n - k - (i - j))*a[i] from d[i][j]
        #       (n-k): size of lu in the final step,
        #       (i-j): current number in lu
        #       (n-k -(i-j)): size of remaining numbers to be assigned to lu

        temp_li = dp[i][j] + a[i] * (i - j - (n - k - (i - j)))

        # Possiblity (2) assign to lu:
        # If a[i] would be assigned to lu:
        #       all the numbers in li needs to be substracted from a[i],
        #       so we add j* a[i] to d[i][j]
        #       Note: substraction of all lu has been done in prevous steps
        #       (see below, 2 lines later)
        #
        #       a[i] WILL be substracted from all future a[x] assigned to li,
        #       so we substract (k-j)*a[i] from d[i][j]
        #       (k-j) is the size of remaining numbers to be assigned to li
        temp_lu = dp[i][j] + a[i] * (j - (k - j))

        # Possiblity (1), both sizes of assigned numbers and li increment by 1
        if dp[i + 1][j + 1] > temp_li:
            dp[i + 1][j + 1] = temp_li

        # Possiblity (2), size of assigned numbers increment by 1, size of li
        # remains the same
        if dp[i + 1][j] > temp_lu:
            dp[i + 1][j] = temp_lu

print(dp[n][k])
print("###########")
print(dp)


