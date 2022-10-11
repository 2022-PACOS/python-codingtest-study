# bfs 접근 풀이
# dfs 풀이도 접근해봐야 할 것 같다.
from collections import deque
 
def bfs(v):
    queue = deque()
    # 출발지 입력
    queue.append(li[v])
    visited[v] = 1
 
    while queue:
        a, b = queue.popleft()
 
        if a == li[-1][0] and b == li[-1][1]:
            return "happy"
 
        for i in range(n + 2):
            # 이미 방문한 곳은 패스
            if visited[i]:
                continue
            if abs(a - li[i][0]) + abs(b - li[i][1]) <= 1000:
                queue.append(li[i])
                visited[i] = 1
 
    # 모든 노드를 돌았는데 페스티벌 장에 도착하지 못하면
    else:
        return "sad"
 
T = int(input())
for _ in range(T):
    n = int(input())
 
    li = []
    for i in range(n + 2):
        li.append(list(map(int, input().split())))
    visited = [0] * (n + 2)
 
    print(bfs(0))