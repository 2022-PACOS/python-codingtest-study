# https://www.acmicpc.net/problem/1915
# 백준 1915번 가장 큰 정사각형
# 메모리: 실패
# 시간: 실패
# 코드길이: 1045B
import sys

array = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    array.append(list(map(int, list(sys.stdin.readline().strip()))))
area = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            a = 0
            for e in range(i, n):
                if array[e][j] == 1:
                    a += 1
                else:
                    break

            b = 0
            for e in range(j, m):
                if array[i][e] == 1:
                    b += 1
                else:
                    break

            value = min(a, b)

            for t in reversed(range(1, value+1)):
                total = 0
                for e1 in range(i, i+t):
                    for e2 in range(j, j+t):
                        if array[e1][e2] == 1:
                            total += 1
                if total == t * t:
                    area[i][j] = total
                    answer = max(answer, total)
                    break
print(answer)


# # 모범답안
# Y, X = map(int, sys.stdin.readline().split())
# graph = []
# for _ in range(Y):
#     graph.append(list(map(int, list(sys.stdin.readline().strip()))))
# result = 0
#
# for i in range(Y):
#     for j in range(X):
#         if i > 0 and j > 0 and graph[i][j] == 1:
#             graph[i][j] += min(graph[i][j-1], graph[i-1][j], graph[i-1][j-1])
#         result = max(result, graph[i][j])
# print(result*result)