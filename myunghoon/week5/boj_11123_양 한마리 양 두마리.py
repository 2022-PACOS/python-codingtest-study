import sys
import queue
def bfs(y,x) :
    # y는 높이, x는 가로 좌표임
    # bfs 탐색으로 visit을 표시한다.
    q = queue.Queue()
    q.put((y,x))
    visit[y][x] = 1
    while q.qsize() != 0:
        now = q.get()
        for i in range(4) :
            ny = now[0] + moves[i][0]
            nx = now[1] + moves[i][1]
            if ny >= 1 and ny <= h and nx >= 1 and nx <=w and visit[ny][nx] != 1 and myMap[ny][nx] == '#':
                q.put((ny,nx))
                visit[ny][nx] = 1

input = sys.stdin.readline

moves = [[-1,0], [1,0], [0,-1], [0,1]]
tc = int(input())
for _ in range(tc) :
    answer = 0
    h,w = map(int, input().split())
    myMap = []
    myMap.append([0]*(w+1))
    visit = [[0]*(w+1) for _ in range(h+1)]
    for i in range(h) :
        tmp = []
        tmp.append(0)
        tmp += list(input().rstrip())
        myMap.append(tmp)

    for i in range(1, h+1) :
        for j in range(1, w+1) : 
            if myMap[i][j] == '#' and visit[i][j] != 1 :
                bfs(i,j)
                answer += 1
    print(answer)