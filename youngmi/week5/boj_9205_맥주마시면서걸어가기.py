# - 기본적으로 가지고있는 맥주는 20병이므로 편의점에 들리지 않고 이동가능한 거리는 20 * 50m = 1000m
# - 시작점에서 편의점 좌표, 페스티벌 좌표를 방문해야하는 노드로 생각하고 bfs를 수행(dfs로도 가능)

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
	queue = deque()
	queue.append((x, y))
	while queue:
		x, y = queue.popleft()
		if abs(x-end_x) + abs(y-end_y) <= 1000:
			print('happy')
			return
		for i in range(n):
			if not visited[i]:
				nx, ny = nodes[i]
				if abs(x-nx) + abs(y-ny) <= 1000:
					queue.append((nx, ny))		
					visited[i] = True
	print('sad')
	return

t = int(input())
for _ in range(t):
	n = int(input())
	start_x, start_y = map(int,(input().split()))
	nodes = [list(map(int, input().split())) for _ in range(n)] # 편의점 좌표
	end_x, end_y = map(int, (input().split()))# 페스티벌 좌표
	visited = [False] * (n+1)
	bfs(start_x, start_y)