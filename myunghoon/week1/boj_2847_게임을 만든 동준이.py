n = int(input())
answer = 0
score = []
for _ in range(n) :
    score.append(int(input()))
max_idx = n-1 #현재 제일 큰 점수값 위치
for i in range(n-1, 0, -1) :
    if score[i] <= score[i-1] :
        answer += score[i-1] - score[i] + 1
        score[i-1] -= (score[i-1] - score[i] + 1)
print(answer)