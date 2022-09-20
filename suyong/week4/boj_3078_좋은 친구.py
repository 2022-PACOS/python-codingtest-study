# https://www.acmicpc.net/problem/3078
# 백준 3078번 좋은 친구
# 메모리: 시간초과
# 시간: 시간초과
# 코드길이: 304B
import sys
n, k = map(int, sys.stdin.readline().split())
answer = 0

arr = []
for i in range(n):
    name = len(list(sys.stdin.readline().strip()))
    arr.append(name)

for i in range(len(arr)):
    for j in range(i+1, i+k+1):
        if j < n and arr[i] == arr[j]:
            answer += 1
print(answer)



# 모범답안
# https://www.acmicpc.net/problem/3078
# 백준 3078번 좋은 친구
# 메모리: 33472KB
# 시간: 2156ms
# 코드길이: 469B
# import sys
# from collections import deque
# n, k = map(int, sys.stdin.readline().split())
# inp = [len(sys.stdin.readline().strip()) for i in range(n)]
# num = [0 for i in range(21)]
#
# cnt = 0
# for i in range(2, 21):
#     q = deque()
#     for leng in inp:
#         q.append(leng)
#         if len(q) > k + 1:
#             if q.popleft() == i:
#                 num[i] -= 1
#         if leng == i:
#             if num[i] > 0:
#                 cnt += num[i]
#             num[i] += 1
# print(cnt)