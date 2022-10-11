import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))

start, end = 0, max(trees) # 시작 점, 끝점

# 이분 탐색 시작
while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in trees:
        if i > mid: # mid보다 큰 나무 높이는 잘림
            tree += i - mid

    if tree >= m: # 더 많이 잘렸다면,
        start = mid + 1
    else: # 덜 잘렸다면,
        end = mid - 1
        
print(end)