# https://www.acmicpc.net/problem/9461
# 백준 9461번 파도반 수열
# 메모리: 30840KB
# 시간: 68ms
# 코드길이: 282B
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    array = [1, 1, 1, 2, 2]
    k = int(sys.stdin.readline())
    if k > 5:
        for i in range(1, k-4):
            array.append(array[i+3]+array[i-1])
        print(array[k-1])
    else:
        print(array[k-1])