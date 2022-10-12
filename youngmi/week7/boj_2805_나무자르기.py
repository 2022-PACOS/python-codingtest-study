# 틀린 코드
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split()) # 나무의 수, 가져가려하는 나무 길이
trees = list(map(int, input().split()))
left, right = 1, max(trees)

while left <= right:
	cut = 0
	mid = (left + right) // 2
	for tree in trees:
		if tree > mid:
			cut += tree - mid
	if cut <= m:
		right = mid - 1
	else:
		left = mid + 1

print(right)
'''

import sys

input = sys.stdin.readline
n, m = map(int, input().split()) # 나무의 수, 가져가려하는 나무 길이
trees = list(map(int, input().split()))
left, right = 1, max(trees)

while left <= right:
	cut = 0
	mid = (left + right) // 2
	print(left, right, mid)
	for tree in trees: # 잘린 나무의 길이 합
		if tree > mid: # mid보다 큰 나무 높이는 잘림
			cut += tree - mid
	if cut >= m: # 원하는 나무 높이보다 더 많이 잘렸으면
		left = mid + 1
	else: # 원하는 나무 높이보다 덜 잘렸으면
		right = mid -1

print(right)