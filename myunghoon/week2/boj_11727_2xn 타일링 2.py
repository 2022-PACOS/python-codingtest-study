'''
dp[i] = dp[i-1] + dp[i-2] + dp[i-2]
      = dp[i-1] + 2*dp[i-2]
'''
import sys
input = sys.stdin.readline
N = int(input())
dp = []

# dp를 구하기 위해서 기저조건 추가함.
dp.append(0) 
dp.append(1)
dp.append(3) 

# dp[n] <- 정답, dp[1],dp[2],dp[3] ...... 구해나감
for i in range(3, N+1) :
    dp.append((2*dp[i-2]) + dp[i-1])

print(dp[N] % 10007)