import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = sorted(list(int(input()) for _ in range(n)))

left, right = 0, min(times) * m
answer = min(times) * m

while left <= right:
	mid = (left + right) // 2
	people = 0
	for t in times:
		people += mid // t
	if people < m:
		left = mid + 1
	else:
		right = mid - 1
		answer = mid

print(answer)