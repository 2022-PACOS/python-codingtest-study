import sys

input = sys.stdin.readline
n = int(input())
times = sorted(list(map(int, input().split()))) # 정렬: O(log n)
# times.sort()를 써도 실행 시간은 동일하다.
total = 0

for i in range(n):
	total += sum(times[:i+1])

print(total)