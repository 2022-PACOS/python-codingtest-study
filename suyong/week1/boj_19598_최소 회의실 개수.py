# import sys
# n = int(sys.stdin.readline())
# array = []
# for i in range(n):
#     start, end = map(int, sys.stdin.readline().split())
#     array.append([start, end])
# array.sort()
# print(array)
#
# room = [array[0][1]]
# for i in range(1, len(array)):
#     if array[i][0] < min(room):
#         room.append(array[i][1])
#     else:
#         room.pop(room.index(min(room)))
#         room.append(array[i][1])
#
# print(len(room))


# --------------------------------------------------------

# 힙을 이용한 모범답안...
import sys
import heapq
n = int(sys.stdin.readline())
array = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    array.append([start, end])

array.sort()

room = []
heapq.heappush(room, array[0][1])

for i in range(1, n):
    if array[i][0] < room[0]:
        heapq.heappush(room, array[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, array[i][1])

print(len(room))