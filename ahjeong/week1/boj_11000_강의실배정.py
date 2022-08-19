import sys
import heapq

N = int(sys.stdin.readline())
sbj = []
for i in range(N):
    sbj.append(list(map(int, sys.stdin.readline().strip().split(' '))))
sbj.sort()

sbj_queue = []
heapq.heappush(sbj_queue, sbj[0][1])

for i in range(1, N):
    if sbj[i][0] < sbj_queue[0]:
        heapq.heappush(sbj_queue, sbj[i][1])
    else:
        heapq.heappop(sbj_queue)
        heapq.heappush(sbj_queue, sbj[i][1])
print(len(sbj_queue))

# 시간초과
# room = [sbj[0][1]]      # 첫번째 원소
# for i in range(1, N):
#     for j in range(len(room)):
#         if  sbj[i][0] >= room[j]:
#             room[j]= sbj[i][1]
#             break
#         else:
#             room.append(sbj[i][1])
# print(len((room)))