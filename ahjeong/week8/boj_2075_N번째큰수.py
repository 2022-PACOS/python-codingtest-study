import sys
import heapq

N = int(sys.stdin.readline())
table = []

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    if not table:
        for i in tmp:
            heapq.heappush(table, i)
    else:
        for i in tmp:
            if table[0] < i:    # 힙의 최솟값보다 클 경우,
                heapq.heappop(table)
                heapq.heappush(table, i)
                

print(table[0])

# # 메모리 초과
# import sys
# import heapq

# N = int(sys.stdin.readline())
# table = []

# for _ in range(N):
#     tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
#     for i in tmp:
#         heapq.heappush(table, (-i, i))

# for _ in range(N):
#     N_max = heapq.heappop(table)

# print(N_max[1])