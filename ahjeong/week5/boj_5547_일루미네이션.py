# 다시 풀어보기
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
visit = [[0]*m for i in range(n)]

def dfs(y, x):
    stack = [(y, x)]
    visit[y][x] = 1
    cnt = 0
    while stack:
        y, x = stack.pop()
        if y%2 : di = [(-1,0), (-1,-1), (0,-1), (0,1), (1,0), (1,-1)]
        else : di = [(-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1)]
        for i, j in di:
            if y+i>=0 and y+i<n and x+j>=0 and x+j<m and not visit[y+i][x+j]:
                if board[y+i][x+j] : cnt+=1
                else :
                    visit[y+i][x+j] = 1
                    stack.append((y+i, x+j))
    return cnt


total = 0
for y in [0, n-1]:
    for x in range(m):
        if board[y][x] :
            total += 2
            if (y==0 and x==m-1) or (y==n-1 and x==0):
                total -= 1
        elif board[y][x]==0 and not visit[y][x]:
            total += dfs(y, x)
for y in range(n):
    for x in [0, m-1]:
        if board[y][x] :
            if (x==0 and y%2) or (x==m-1 and y%2==0) : total +=3
            else : total += 1
        elif board[y][x]==0 and not visit[y][x]:
            total += dfs(y, x)
            
print(total)