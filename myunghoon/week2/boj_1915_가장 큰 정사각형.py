'''
dp[i][j] = (i,j) 좌표를 맨 오른쪽 아래로 둔 최대 정사각형 넓이
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
'''
n, m = map(int, input().split())

myMap = []
dp= []
answer = 0
for _ in range(n) :
    myMap.append(list(map(int, list(input()))))

dp = [[0 for _ in range(m)] for _ in range(n)]

# 기저조건
dp[0] = myMap[0]
for i in range(n) : 
    dp[i][0] = myMap[i][0]

# dp채우기
for i in range(1, n) :
    for j in range(1, m) :
        if myMap[i][j] == 1 :
            if dp[i-1][j-1] and dp[i-1][j] and dp[i][j-1] : 
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1]) + 1
            else : 
                dp[i][j] = 1
        else :
            dp[i][j] = 0

for i in range(n) :
    for j in range(m) :
        answer = max(answer,dp[i][j])
print(answer**2)