'''
dp[i] = P(i), 즉 i번째의 파도반 수열 정삼각형 변의 길이
dp[i] = dp[i-1] + dp[i-5]
'''
testcase = int(input())
for _ in range(testcase) :
    N = int(input())
    dp = [0] * 101

    # 기저 조건
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    # dp 채우기
    for i in range(6, N+1) : 
        dp[i] = dp[i-1] + dp[i-5]
    
    print(dp[N])