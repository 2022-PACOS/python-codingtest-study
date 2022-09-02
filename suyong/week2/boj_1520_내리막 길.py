# https://www.acmicpc.net/problem/1520
# 백준 1520번 내리막 길
# 메모리: 실패
# 시간: 실패
# 코드길이: 1644B
import sys

array = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    array.append(list(map(int, list(sys.stdin.readline().split()))))
road = []
answer = 0
visit = [[0] * m for _ in range(n)]
visit[0][0] = 1

print(array)
print(visit)


def dfs(i, j):
    global answer
    # 상 (i-1, j)
    if i-1 >= 0 and visit[i-1][j] == 0 and array[i][j] > array[i-1][j]:
        visit[i-1][j] = 1
        print(visit)
        dfs(i-1, j)
        visit[i-1][j] = 0
        print(visit)
    # 하 (i+1, j)
    if i+1 < n and visit[i+1][j] == 0 and array[i][j] > array[i+1][j]:
        if i+1 == n-1 and j == m-1:
            visit[i+1][j] = 1
            answer += 1
            print(visit)
            visit[i+1][j] = 0
            return
        else:
            visit[i+1][j] = 1
            print(visit)
            dfs(i+1, j)
            visit[i+1][j] = 0
            print(visit)
    # 좌 (i, j-1)
    if j-1 >= 0 and visit[i][j-1] == 0 and array[i][j] > array[i][j-1]:
        visit[i][j-1] = 1
        print(visit)
        dfs(i, j-1)
        visit[i][j-1] = 0
        print(visit)
    # 우 (i, j+1)
    if j+1 < m and visit[i][j+1] == 0 and array[i][j] > array[i][j+1]:
        if i == n-1 and j+1 == m-1:
            visit[i][j+1] = 1
            answer += 1
            print(visit)
            visit[i][j+1] = 0
            return
        else:
            visit[i][j+1] = 1
            print(visit)
            dfs(i, j+1)
            visit[i][j+1] = 0
            print(visit)
    # 갈데가 없을때 (상, 하, 좌, 우)
    if (i-1 < 0 or visit[i-1][j] == 1 or array[i][j] < array[i-1][j]) and \
        (i+1 >= n or visit[i+1][j] == 1 or array[i][j] < array[i+1][j]) and \
        (j-1 < 0 or visit[i][j-1] == 1 or array[i][j] < array[i][j-1]) and \
        (j+1 >= m or visit[i][j+1] == 1 or array[i][j] < array[i][j+1]):
        return


dfs(0, 0)
print(road)
print(answer)


# # 모범답안 (DFS + DP)
# import sys
#
# input = sys.stdin.readline
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def dfs(x, y):
#     if x == m-1 and y == n-1:
#         return 1
#     if c[x][y] != -1:
#         return c[x][y]
#     c[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n:
#             if a[nx][ny] < a[x][y]:
#                 c[x][y] += dfs(nx, ny)
#     return c[x][y]
#
#
# m, n = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(m)]
# c = [[-1]*n for _ in range(m)]
# print(dfs(0, 0))