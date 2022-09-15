import sys
from collections import deque
 
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
len_count = [0] * 21
 
queue = deque()
answer = 0
for i in range(N):
    student = len(input().rstrip())
    if i > K:
        len_count[queue.popleft()] -= 1
    answer += len_count[student]
    queue.append(student)
    len_count[student] += 1
 
print(answer)