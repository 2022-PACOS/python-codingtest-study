import sys
from collections import deque

def mapCheck(x,y) : 
    # 좌표가 맵 내에 있는지 아닌지 검사한다.
    # 이동 가능한 좌표면 1을 리턴하고 아니면 0을 리턴한다.
    global N,M
    if x>=0 and x<N and y>=0 and y<M :
        return 1
    else :
        return 0
def BFS() :
    '''
    N*M 크기의 Board 에서 BFS를 한 결과가 T 시간 내로 들어오면 그 최단시간을 반환한다.
    '''
    global N,M,T
    answer = 10001
    queue = deque()
    queue.append((0,0,0)) #(x,y,h) x:x좌표, y:y좌표, h:x,y에 도달한 시간
    visit[0][0] = 1
    while(queue) :
        x,y,h = queue.popleft()
        if x == N-1 and y == M-1 : 
            answer = min(answer, h)
        for i in range(4) :
            nx = x+diff[i][0]
            ny = y+diff[i][1]
            nh = h+1
            if mapCheck(nx,ny) and visit[nx][ny] != 1:
                if board[nx][ny] == 0 : 
                    queue.append((nx,ny,nh))
                    visit[nx][ny] = 1
                elif board[nx][ny] == 2 : #gram인 경우
                    answer = min(answer, nh + (N-1-nx) + (M-1-ny))
                    visit[nx][ny] = 1
    return answer
        
input = sys.stdin.readline
N,M,T = map(int, input().split())
board = list(list(map(int,input().split())) for _ in range(N)) # N*M 크기의 board 생성
visit = [[0] * M for _ in range(N)]
diff = [[-1,0],[0,1],[1,0],[0,-1]] #위,오른쪽,아래쪽,왼쪽
answer = BFS()
if answer > T : print("Fail")
else : print(answer)