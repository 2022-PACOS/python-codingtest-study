# https://www.acmicpc.net/problem/1406
# 백준 1406번 에디터
# 메모리: 시간초과
# 시간: 시간초과
# 코드길이: 485B
import sys

n = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())

curser = len(n)

for _ in range(m):
    temp = sys.stdin.readline().strip()
    if list(temp)[0] == 'L' and curser > 0:
        curser -= 1
    if list(temp)[0] == 'D' and curser < len(n):
        curser += 1
    if list(temp)[0] == 'B' and curser > 0:
        n.pop(curser-1)
        curser -= 1
    if list(temp)[0] == 'P':
        n.insert(curser, list(temp)[2])
        curser += 1
print(''.join(n))



# 모범답안
# https://www.acmicpc.net/problem/1406
# 백준 1406번 에디터
# 메모리: 40672KB
# 시간: 376ms
# 코드길이: 494B
# import sys
#
# stack_l = list(sys.stdin.readline().strip())
# stack_r = []
# m = int(sys.stdin.readline())
#
# for i in range(m):
#     command = sys.stdin.readline().split()
#
#     if command[0] == "L" and stack_l:
#         stack_r.append(stack_l.pop())
#     elif command[0] == "D" and stack_r:
#         stack_l.append(stack_r.pop())
#     elif command[0] == "B" and stack_l:
#         stack_l.pop()
#     elif command[0] == "P":
#         stack_l.append(command[1])
#
# print("".join(stack_l + list(reversed(stack_r))))
