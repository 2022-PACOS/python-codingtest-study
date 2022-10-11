# 한개의 리스트 대신 2개의 스택을 사용.
import sys
st1 = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
command = [sys.stdin.readline().rstrip().split(' ') for _ in range(n)]
st2 = []


for cmd in command:
    if cmd[0] == 'L':
        if st1: # 현재 커서가 문장의 맨 앞이면
            st2.append(st1.pop())
    elif cmd[0] == 'D':
        if st2: # 현재 커서가 문장의 맨 뒤이면
            st1.append(st2.pop())
    elif cmd[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(cmd[1])    
        
st1.extend(reversed(st2))   # 스택의 순서 고려
print(''.join(st1))