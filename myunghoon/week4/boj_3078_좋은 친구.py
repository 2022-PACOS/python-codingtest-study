import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
nameSize = []    # 이름 길이
answer = 0 # 정답, 좋은친구 쌍

for _ in range(21):
    nameSize.append(deque([]))

for i in range(n):
    friendNameLen = len(sys.stdin.readline().strip()) 
    while True:
        if len(nameSize[friendNameLen]) == 0:    
            nameSize[friendNameLen].append(i)    # 등수를 삽입해준다
            break
        # 새로 들어오는 등수와 비교해서 k 보다 같거나 작으면 append한다.
        if i - nameSize[friendNameLen][0] <= k:
            answer += len(nameSize[friendNameLen])
            nameSize[friendNameLen].append(i)
            break
        # k범위보다 초과하면 처음들어온 등수부터 pop
        if i - nameSize[friendNameLen][0] > k:
            nameSize[friendNameLen].popleft()
            continue
print(answer)