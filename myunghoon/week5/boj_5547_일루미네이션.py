import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
move=[[(-1,0), (-1,-1), (0,-1), (0,1), (1,0), (1,-1)],[(-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1)]]
m, n = map(int, input().split())
myMap = [list(map(int, input().split())) for i in range(n)]
visit = [[0]*m for i in range(n)]
total = 0

# 연결된 0인 칸 탐색 후 테두리 개수 반환
def dfs(y, x):
    visit[y][x] = 1
    cnt = 0
    if y % 2 == 1 : #홀수행일때 1,3,5,7,9 ...  
        for i, j in move[0]:
            if y+i>=0 and y+i<n and x+j>=0 and x+j<m:
                if myMap[y+i][x+j] == 1:
                    cnt+=1
                elif myMap[y+i][x+j] == 0 and not visit[y+i][x+j] :
                    cnt += dfs(y+i,x+j)
    else : #짝수행일때 2 4 6...  
        for i, j in move[1]:
            if y+i>=0 and y+i<n and x+j>=0 and x+j<m and not visit[y+i][x+j]:
                if myMap[y+i][x+j] == 1:
                    cnt+=1
                elif myMap[y+i][x+j] == 0 and not visit[y+i][x+j] :
                    cnt += dfs(y+i,x+j)
    return cnt

# 가장 바깥쪽 테두리 탐색
# 맨 위, 맨 아래 행 탐색
for y in [0, n-1]: 
    for x in range(m):
        if myMap[y][x] :
            total += 2
            if n % 2 == 1 :   # 짝수행에서 튀어나온 캡모양 있을 때
                if (y==0 and x==m-1) or (y==n-1 and x==m-1): 
                    total -= 1
            else :            # 홀수행에서 튀어나온 캡모양 있을 때
                if (y==0 and x==m-1) or (y==n-1 and x==0):
                    total -= 1
        elif myMap[y][x]==0 and not visit[y][x]:
            total += dfs(y, x)
# 맨 왼쪽, 맨 오른쪽 열 탐색
for x in [0, m-1]:
    for y in range(n): 
        if myMap[y][x] :
            if (x==0 and y%2) or (x==m-1 and y%2==0) : total +=3
            else : total += 1
        elif myMap[y][x]==0 and not visit[y][x]:
            total += dfs(y, x)
            
print(total)