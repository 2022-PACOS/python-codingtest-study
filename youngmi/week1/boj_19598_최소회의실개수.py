import sys
import heapq

input = sys.stdin.readline
n = int(input())
times = [list(map(int,input().split())) for _ in range(n)]
times.sort(key=lambda x: x[0])
heap = []
heapq.heappush(heap, times[0][1])

for i in range(1, n):
	if heap[0] > times[i][0]:
		heapq.heappush(heap, times[i][1])
	else:
		heapq.heappop(heap)
		heapq.heappush(heap, times[i][1])

print(len(heap))