import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
myList = []
for i in range(n) :
    a,b = map(int, input().split())
    myList.append([a,b])
myList.sort() # 끝나는 시간과 다음 시작시간과 비교해서 회의실의 개수를 구하기 위해서임.
heap = []
# 최초시작시간의 끝나는 시간을 넣음.
heappush(heap, myList[0][1])

for i in range(1, n) :
    # 다음 시작시간과 비교한다.
    # 만약 다음 시작시간보다 현재 끝나는 시간이 더 크다면, 강의실을 추가해야한다. 즉 heapqueue에 넣어야한다는 말이다.
    if heap[0] > myList[i][0] :
        heappush(heap,myList[i][1])
    else :
        heappush(heap,myList[i][1])
        heappop(heap)
print(len(heap))