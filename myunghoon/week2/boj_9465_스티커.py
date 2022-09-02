'''
dp[0][i] = 0행의 i번째 점수를 획득했을 때의 최대값
dp[1][i] = 1행의 i번째 점수를 획득했을 때의 최대값
'''

testcase = int(input())

for _ in range(testcase) :
    answer = 0
    N = int(input())
    score = []
    for _ in range(2) : 
        score.append(list(map(int,input().split())))
    dp=[[0 for _ in range(N)] for _ in range(2)]

    # 기저 조건
    if N < 2:
        dp[0][0] = score[0][0]
        dp[1][0] = score[1][0]
        answer = max(dp[0][0],dp[1][0])
    else :
        dp[0][0] = score[0][0]
        dp[1][0] = score[1][0]
        dp[0][1] = score[1][0] + score[0][1]
        dp[1][1] = score[1][1] + score[0][0]
        answer = max(dp[0][1],dp[1][1])
    
    # dp 채우기
    for i in range(2,N) :
        dp[0][i] = max(score[0][i]+dp[1][i-1], score[0][i]+dp[1][i-2])
        dp[1][i] = max(score[1][i]+dp[0][i-1], score[1][i]+dp[0][i-2])
        answer = max(dp[0][i], dp[1][i])

    print(answer)