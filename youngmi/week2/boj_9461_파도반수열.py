# 점화식 dp[i] = dp[i-1] + dp[i-5] (i>5)
n = int(input())
t = [int(input()) for _ in range(n)]
dp = [0,1,1,1,2,2]

for i in range(6, max(t)+1):
    dp.append(dp[i-1] + dp[i-5])

for i in t:
    print(dp[i])

# 피보나치 수열
p = [0] * 101
p[1], p[2], p[3] = 1, 1, 1
for i in range(4, 101):
    p[i] = p[i-3] + p[i-2]

n = int(input())
for i in range(n):
    t = int(input())
    print(p[t])