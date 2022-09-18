import sys
from collections import deque

N, K = map(int, input().split(' '))
names = [len(sys.stdin.readline().rstrip()) for _ in range(N)]
# ['IVA', 'IVO', 'ANA', 'TOM']
# [3, 3, 3, 3]  # 이름 길이
# [0, 1, 2, 3]  # 등수
n_q = [deque() for _ in range(21)]
real = 0

# i: 등수 - 1, v: 이름 길이
for i, v in enumerate(names):
    # 큐가 비어있지 않고 & 큐[0] 학생이 기준학생(i)과 K 이상 차이나면 그 학생 제외
    while n_q[v] and i-n_q[v][0] > K:
        n_q[v].popleft()    # 기준 학생을 기준으로 K 이상 차이나니까 제외
    
    if n_q[v]:
        real += len(n_q[v]) # 현재 큐안의 가능한 친구들 수
    n_q[v].append(i)
    
print(real)

# 처음 풀이
# 오류: 문제에서 '몇 쌍' 이라는 말이 2명을 하나로 묶는 것 뿐만 아니라 2명 이상의 묶음까지 생각했었다.
# 국립국어원에 '쌍'은 둘을 하나로 묶어 세는 단위라고 표기되어 있음.
# 이상한 곳에서 고민했다.
# N, K = map(int, input().split(' '))
# names = [sys.stdin.readline().rstrip() for _ in range(N)]
# # ['IVA', 'IVO', 'ANA', 'TOM']
# # [0, 1, 2, 3]

# n_q = deque()
# real = 0

# while K:
#     for i in range(N):
#         if i+K+1 <= N:
#             n_q.append(names[i:i+K+1])
#         else:
#             K -= 1
#             break

# print(n_q)
# while n_q:
#     friends = n_q.popleft()
#     for s in range(len(friends)-1):
#         if len(friends[s]) != len(friends[s+1]):
#             break
#         else:
#             if s == len(friends)-2:
#                 real += 1
# print(real)