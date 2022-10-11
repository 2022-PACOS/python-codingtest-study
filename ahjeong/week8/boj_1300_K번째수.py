# # 메모리초과
# import sys
# import heapq

# input = sys.stdin.readline
# N = int(input())
# k = int(input())
# B = []

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         heapq.heappush(B, i*j)
#         if len(B) == k:
#             for _ in range(k-1):
#                 heapq.heappop(B)
#             print(B[0])
#             break

# 시간초과
# import sys
# import heapq

# input = sys.stdin.readline
# N = int(input())
# k = int(input())
# B = []
# count = 0

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         count += 1
#         if count == 1:
#             heapq.heappush(B, (-(i*j), (i*j)))
#         else:
#             if B[0][1] < (i*j):
#                 heapq.heappush(B, (-(i*j), (i*j)))
#             else:
#                 pass
#         if count == k:
#             print(B[0][1])
#             break


# 이진 탐색
N = int(input())
k = int(input())

# 1 ~ k 까지 조건을 만족하는 숫자를 찾는다.
start, end = 0, k   # K번째 수는 K를 넘을 수 없다.

answer = 0

while start <= end:
    mid = (start+end) // 2
    count = 0
    
    # 모든 행을 살피며 mid 이하인 값의 개수를 찾는다.
    for i in range(1, N+1):
        # 1. i번째 행에서 mid 이하의 값을 만족하는 값의 개수를 찾는다. -> mid // i
        # 2. N=1000인 경우, mid는 50만이 되는데 이 때 mid//i > N 이 되므로
        #    i번째 행을 이루는 숫자 개수인 N을 넘어가지 않도록 해준다. -> min(mid//i, N)
        count += min(mid//i, N)
        
    # mid이하의 개수가 k보다 작다면 mid 이하의 숫자들은 볼 필요도 없으므로
    if count < k:
        start = mid+1
    else:   # mid 위의 숫자들은 볼 필요 없으므로.
        answer = mid
        end = mid-1
        
print(answer)