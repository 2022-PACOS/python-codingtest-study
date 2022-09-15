# https://www.acmicpc.net/problem/9205
# 백준 9205번 맥주 마시면서 걸어가기
# 메모리: 30840KB
# 시간: 80ms
# 코드길이: 699B
# 풀이: https://yongyongtv.tistory.com/29
import sys
T = int(sys.stdin.readline())


def dfs(x, y, check):
    global success
    visit[check] = 1
    if x == arr[len(arr)-1][0] and y == arr[len(arr)-1][1]:
        success = 1
        print("happy")
        return
    for i in range(len(arr)):
        if success:
            return
        if abs(arr[i][0] - x) + abs(arr[i][1] - y) <= 1000 and visit[i] == 0:
            dfs(arr[i][0], arr[i][1], i)


for _ in range(T):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n+2):
        arr.append(list(map(int, sys.stdin.readline().split())))
    visit = [0 for _ in range(len(arr))]
    success = 0
    dfs(arr[0][0], arr[0][1], 0)
    if not success:
        print("sad")