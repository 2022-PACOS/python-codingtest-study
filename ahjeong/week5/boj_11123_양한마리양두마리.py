n = int(input())

# dfs
def dfs(x, y):
    if x<= -1 or x >= H or y <= -1 or y >= W:
        return False
    print(x, y)
    if graph[x][y] == '#':
        graph[x][y] = '.'
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for _ in range(n):
    H, W = map(int, input().split())
    graph = [list(input() for _ in range(H))]
    count = 0
    for i in range(H):
        for j in range(W):
            if dfs(i, j) == True:
                count += 1
    print(count)

import sys
sys.setrecursionlimit(100000)

T = int(input())        # 입력 받을 테스트 케이스의 수

# dfs
def dfs(y, x):
    graph[y][x] = '.'   # 이미 방문한 곳은 '.' 으로 표시
    dy = [0,1,0,-1]     # 상하좌우로 탐방할 좌표값 설정
    dx = [1,0,-1,0]
    for k in range(4):      # 상하좌우에 '#'이 있는지
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and nx >= 0 and ny < H and nx < W:   # 지정 범위를 벗어 나지 않는 선에서 확인 하기
            if graph[ny][nx] == '#':    # '#'을 발견했으면 다시 그 자리에서 재귀 호출
                dfs(ny, nx)

for _ in range(T):
    H,W = map(int, input().split())     # 그리드의 높이(H)와 너비(W) 입력받기
    graph = [list(input()) for _ in range(H)]   # 양과 풀의 그리드 정보를 저장할 수 있는 공간 설정
    count = 0   # 몇 개의 양 무리가 있는지 카운트 할 변수
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':  # 양이 발견 됐을 경우
                dfs(i, j)
                count += 1  # 하나의 무리 발견 (카운트 추가)

    print(count)
    
    
