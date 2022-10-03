import sys
from collections import deque
def BFS(x,y) :
    '''
    x,y 를 시작으로 BFS 탐색을 하는데 페스티벌에 도착할수있으면 happy,  못하면 sad를 출력하는 함수
    '''
    global targetX,targetY
    flag = False
    q = deque()
    visit = []
    q.append((x,y))
    visit.append((x,y))
    while q :
        nx,ny = q.popleft()
        if nx == targetX and ny == targetY :
            print("happy")
            flag = True
            break
        for [x,y] in myMap :
           if (x,y) not in visit : 
             if abs(nx-x) + abs(ny-y) <= 1000 :
                q.append((x,y))
                visit.append((x,y))   
    if flag == False : print("sad")
input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    n = int(input())
    x,y = map(int, input().split())
    myMap = [list(map(int,input().split()))for _ in range(n)]
    targetX, targetY = map(int, input().split())
    myMap.append([targetX,targetY])
    BFS(x,y)