# https://www.acmicpc.net/problem/17836
# 백준 17836번 공주님을 구해라!
# 메모리: 32508KB
# 시간: 140ms
# 코드길이: 1274B
# BFS
import sys
from collections import deque
n, m, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visit = [[0] * m for _ in range(n)]
visit_sword = [[0] * m for _ in range(n)]
visit[0][0] = 1
visit_sword[0][0] = 1

q = deque()
q.append((0, 0, 0, 0))

while q:
    x, y, move, sword = q.popleft()
    if x == n-1 and y == m-1:
        if not answer:
            answer = move
        else:
            answer = min(answer, move)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 칼 쥔상태
        if 0 <= nx < n and 0 <= ny < m and sword and visit_sword[nx][ny] == 0:
            visit_sword[nx][ny] = 1
            q.append((nx, ny, move + 1, 1))
        # 칼 못쥔상태, 벽을 만나지 않음
        elif 0 <= nx < n and 0 <= ny < m and not sword and visit[nx][ny] == 0 and arr[nx][ny] != 1:
            if arr[nx][ny] == 2:
                visit_sword[nx][ny] = 1
                q.append((nx, ny, move + 1, 1))
            else:
                visit[nx][ny] = 1
                q.append((nx, ny, move + 1, 0))

if answer:
    if answer <= T:
        print(answer)
    else:
        print("Fail")
else:
    print("Fail")


# https://www.acmicpc.net/problem/17836
# 백준 17836번 공주님을 구해라!
# 메모리: 실패
# 시간: 시간초과
# 코드길이: 1258B
# DFS (시간초과)
# import sys
# sys.setrecursionlimit(100000)
# n, m, T = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# answer = 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# visit = [[0] * m for _ in range(n)]
# visit[0][0] = 1
#
#
# def dfs(x, y, move, sword):
#     global answer
#     if x == n-1 and y == m-1:
#         if not answer:
#             answer = move
#             return
#         else:
#             answer = min(answer, move)
#             return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 칼 쥔상태
#         if 0 <= nx < n and 0 <= ny < m and sword and visit[nx][ny] == 0:
#             visit[nx][ny] = 1
#             dfs(nx, ny, move + 1, 1)
#             visit[nx][ny] = 0
#         # 칼 못쥔상태, 벽을 만나지 않음
#         elif 0 <= nx < n and 0 <= ny < m and not sword and visit[nx][ny] == 0 and arr[nx][ny] != 1:
#             if arr[nx][ny] == 2:
#                 visit[nx][ny] = 1
#                 dfs(nx, ny, move + 1, 1)
#                 visit[nx][ny] = 0
#             else:
#                 visit[nx][ny] = 1
#                 dfs(nx, ny, move + 1, 0)
#                 visit[nx][ny] = 0
#
#
# dfs(0, 0, 0, 0)
# if answer:
#     if answer <= T:
#         print(answer)
#     else:
#         print("Fail")
# else:
#     print("Fail")