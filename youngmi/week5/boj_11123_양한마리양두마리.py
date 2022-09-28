# bfs(큐)나 dfs(스택)로 구현가능한 문제, dfs로 풀이
# #이 상하좌우에 있는지 확인한다.
# 연결되어 있으면 하나의 무리로 판단
# dfs 호출횟수를 카운트 한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 파이썬은 재귀 깊이 제한을 풀어줘야 한다.

pos = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 좌, 우, 상, 하

def dfs(x, y):
	if x<0 or y<0 or x>=h or y>=w:
		return False
	if graph[x][y] == '#':
		graph[x][y] = '.'
		for dx, dy in pos:
			dfs(x + dx, y + dy)
		return True
	return False

t = int(input())
for _ in range(t):
	count = 0
	h, w = map(int, input().split())
	graph = [list(input().strip()) for _ in range(h)]
	for x in range(h):
		for y in range(w):
			if dfs(x, y) == True:
				count += 1

	print(count)