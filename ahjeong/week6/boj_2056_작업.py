# 위상정렬 + Dynamic Programming
import sys
input = sys.stdin.readline

n = int(input())
costs = [0 for _ in range(n+1)] # dp배열
graph = [[] for _ in range(n+1)]


for i in range(1, n+1):
    cost, m, *lst = map(int, input().split())
    costs[i] = cost
    for x in lst:
        graph[i].append(x)

for i in range(1, n+1):
    tmp = 0
    for j in graph[i]:
        tmp = max(tmp, costs[j])
    costs[i] += tmp

# 가장 큰 비용 값 출력
print(max(costs))


# for문 1묶음 만 쓴 코드

# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     N = int(input())
#     costs = [0]*(N+1)

#     for i in range(1, N+1):
#         cur_input = list(map(int, input().split()))

#         prev_max_time = 0
#         for j in range(2, 2 + cur_input[1]):
#             prev_max_time = max(prev_max_time, costs[cur_input[j]])

#         costs[i] = prev_max_time + cur_input[0]

#     print(max(costs))