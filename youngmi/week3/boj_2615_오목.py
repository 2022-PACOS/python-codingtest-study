import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
	for y in range(19):
		now = board[x][y]
		if now:
			for i in range(4):
				count = 1
				nx, ny = x + dx[i], y + dy[i]
				while 0 <= nx <19 and 0 <= ny < 19 and board[nx][ny] == now:
					count += 1
					if count == 5:
						# 육목 체크
						if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == now:
							break
						if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == now:
							break
						# 육목이 아니면 성공한거니까 종료
						print(now)
						print(x+1, y+1)
						exit(0)

					nx += dx[i]
					ny += dy[i]
print(0)