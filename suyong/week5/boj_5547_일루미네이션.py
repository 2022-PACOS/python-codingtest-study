# https://www.acmicpc.net/problem/5547
# 백준 5547번 일루미네이션
# 메모리: 실패
# 시간: 실패
# 코드길이: 실패


# 모범답안
import sys
from collections import deque

w, h = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

graph = deque(graph)
graph.appendleft([0] * w)
graph.append([0] * w)

graph = list(graph)
for i in range(h + 2):
    graph[i].insert(0, 0)
    graph[i].append(0)

visit = [[-1] * (w + 2) for _ in range(h + 2)]

odd_x = [0, 0, +1, +1, -1, -1]
odd_y = [-1, +1, 0, +1, 0, +1]
even_x = [0, 0, +1, +1, -1, -1]
even_y = [-1, +1, -1, 0, -1, 0]

wall_cnt = 0

q = deque()
q.append((0, 0))
visit[0][0] = 1

while q:
    x, y = q.popleft()

    if x % 2 == 0:  # 짝수
        for k in range(6):
            nx = x + even_x[k]
            ny = y + even_y[k]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if graph[nx][ny] == 0:
                    if visit[nx][ny] == -1:  # 만약 방문하지 않았다면
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                else:
                    wall_cnt += 1

    else:  # 홀수
        for k in range(6):
            nx = x + odd_x[k]
            ny = y + odd_y[k]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if graph[nx][ny] == 0:
                    if visit[nx][ny] == -1:  # 만약 방문하지 않았따면
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                else:
                    wall_cnt += 1

print(wall_cnt)