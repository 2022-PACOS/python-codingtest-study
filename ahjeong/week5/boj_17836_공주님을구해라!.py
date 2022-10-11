from collections import deque

def bfs():
    princess=10001

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited[0][0] = 1
    queue=deque([(0,0)])

    # queue 가 빌 때까지
    while queue:
        x, y = queue.popleft()
        if Mat[x][y] == 2:
            princess=abs(N-1-x) + abs(M-1-y) + visited[x][y]-1

        if (x,y) == (N-1,M-1):
            return min(visited[x][y]-1, princess)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and Mat[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return princess


N, M, T= map(int, input().split())

Mat= [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

res = bfs()

if res<=T:
    print(res)
else:
    print("Fail")