# https://www.acmicpc.net/problem/13335
# 백준 13335번 트럭
# 메모리: 32440KB
# 시간: 124ms
# 코드길이: 505B
import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))

q = deque([0 for i in range(w-1)])
q.append(truck[0])
next = 1
times = 1
print(times, "번째: ", q)
print("next: ", next)

while q:
    if next < n:
        q.popleft()
        if sum(q) + truck[next] <= L:
            q.append(truck[next])
            next += 1
            times += 1
        else:
            q.append(0)
            times += 1
    else:
        q.popleft()
        times += 1
    print(times, "번째: ", q)
    print("next: ", next)
print(times)