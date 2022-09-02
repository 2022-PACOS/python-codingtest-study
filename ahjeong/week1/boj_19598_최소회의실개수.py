import sys
import heapq

N = int(sys.stdin.readline())
conf = []
for i in range(0, N):
    conf.append(list(map(int, sys.stdin.readline().strip().split(' '))))

conf.sort()
conf_queue = []
heapq.heappush(conf_queue, conf[0][1])

for i in range(1, N):
    if conf[i][0] < conf_queue[0]:
        heapq.heappush(conf_queue, conf[i][1])
    else:
        heapq.heappop(conf_queue)
        heapq.heappush(conf_queue, conf[i][1])

print(len(conf_queue))
        