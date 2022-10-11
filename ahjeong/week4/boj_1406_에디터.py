# 시간초과
# 주의할 점: 리스트의 insert, delete, remove의 시간복잡도는 O(N) 이다.
from collections import deque
import sys

s = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
order = [sys.stdin.readline().rstrip().split(' ') for _ in range(n)]

order_q = deque(order)
s.append('_')

while order_q:
    o = order_q.popleft()   # 명령어
    if o[0] == 'L':
        cursor = s.index('_')   # 현재 커서가 위치하는 곳
        if cursor == 0:  # 현재 커서가 문장의 맨 앞이면
            pass
        else:   # 커서를 왼쪽으로 한 칸 옮김('_'의 위치를 바꿈)
            tmp = s[cursor-1]
            s[cursor-1] = '_'
            s[cursor] = tmp
    elif o[0] == 'D':
        cursor = s.index('_')
        if cursor == len(s)-1:  # 현재 커서가 문장의 맨 뒤이면
            pass
        else:   # 커서를 오른쪽으로 한 칸 옮김('_'의 위치를 바꿈)
            tmp = s[cursor+1]
            s[cursor+1] = '_'
            s[cursor] = tmp
            
    elif o[0] == 'B':
        cursor = s.index('_')
        if cursor == 0:
            pass
        else:
            del s[cursor-1] # 커서 왼쪽에 있는 문자를 삭제함.
    else:   # P
        cursor = s.index('_')
        s = s[:cursor] + list(o[1])+ s[cursor:]
s.remove('_')         
print(''.join(s))