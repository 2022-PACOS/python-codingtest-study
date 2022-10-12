import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []
heapq.heapify(heap)
for _ in range(N) :
    numbers = list(map(int, input().split()))
    for elem in numbers :
        if len(heap) == N: 
            if elem > heap[0] :
                heapq.heappop(heap)
                heapq.heappush(heap, elem)
        else :
            heapq.heappush(heap,elem)
print(heap[0])