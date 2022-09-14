# https://www.acmicpc.net/problem/11123
# 백준 11123번
# 메모리: 40748KB
# 시간: 316ms
# 코드길이: 750B
import sys
sys.setrecursionlimit(100000)
T = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, isStart):
    global cnt
    visit[x][y] = 1

    for index in range(4):
        nx = x + dx[index]
        ny = y + dy[index]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '#' and visit[nx][ny] == 0:
            dfs(nx, ny, 0)

    if isStart:
        cnt += 1


for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
    cnt = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#' and visit[i][j] == 0:
                dfs(i, j, 1)

    print(cnt)