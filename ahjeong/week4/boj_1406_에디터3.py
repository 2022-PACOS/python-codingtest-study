# 덱(deque) 사용
import sys
from collections import deque

st1 = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
command = [sys.stdin.readline().rstrip().split(' ') for _ in range(n)]
dq = deque([])


for cmd in command:
    if cmd[0] == 'L':
        if st1: # 현재 커서가 문장의 맨 앞이면
            dq.appendleft(st1.pop())
    elif cmd[0] == 'D':
        if dq: # 현재 커서가 문장의 맨 뒤이면
            st1.append(dq.popleft())
    elif cmd[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(cmd[1])    
        
print(''.join(st1 + list(dq)))