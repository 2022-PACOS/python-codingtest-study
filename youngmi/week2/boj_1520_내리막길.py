import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    # 도착 지점에 도달하면 1 리턴
    if x == m-1 and y == n-1:
        return 1
     # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
print(dfs(0, 0))

import sys