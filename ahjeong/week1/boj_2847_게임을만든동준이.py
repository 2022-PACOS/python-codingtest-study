import sys

N = int(input())
level = [int(sys.stdin.readline().strip()) for i in range(N)]
level.reverse()

count = 0
top = level[0]

for i in range(1, N):
    if level[i] >= level[i-1]:
        count += level[i] - (level[i-1] - 1)
        level[i] = level[i-1] - 1

print(count)
        

# for i in range(0, N):
#     if level[i] - (top-i) > 0:
#         count += level[i] - (top-i)
# print(count)  
# 예외: 2, 3, 5, 7