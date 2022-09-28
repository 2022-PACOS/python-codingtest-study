# - (0,0)부터 (n-1,m-1)까지 bfs로 풀어서 최단거리를 구한 것과 (0,0)부터 그람의 위치까지 거리 + 그람의 위치에서 (n-1, m-1)의 직선거리를 합한 것을 비교해서 최소 값을 구한다.
# - 최소값이 T보다 작다면 해당 값을 출력하고 T 초과이면 “Fail”을 출력
# - 1은 이동할 수 없는 공간이기 때문에 0을 따라서 움직인다.
# - visit 배열에 +1씩 하면서 최소 이동거리를 구한다.
# - 그람을 사용하는 경우는 그람 도달 전까지의 시간과 그람을 사용해서 마지막 지점까지 가는 시간의 합을 gram변수에 저장한다.
# - 마지막 지점에 도달하면 최솟값을 return하고 도달하지 못하면 gram을 return한다


import sys
from collections import deque

def bfs(x, y):
	global gram
	queue = deque([(x, y)])
	visited[x][y] = 1
	while queue:
		x, y = queue.popleft()
		if graph[x][y] == 2: # 그람이 있다면
			gram = visited[x][y]-1 + abs(n-1-x) + abs(m-1-y) # 그람의 위치에서 [n-1][m-1]까지 거리
		if x == n-1 and y == m-1:
			return min(visited[-1][-1] - 1, gram)
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
				if visited[nx][ny] == 0 :
					visited[nx][ny] = visited[x][y] + 1
					queue.append((nx, ny))
				
	return gram # 공주님한테 까지 못간 경우

input = sys.stdin.readline
n, m ,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 성 구조
visited = [[0] * m for _ in range(n)] # 방문 여부
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
gram = 100001

answer = bfs(0,0)
print("Fail" if answer > t else answer)