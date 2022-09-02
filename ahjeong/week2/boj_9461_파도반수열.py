import sys

N = int(sys.stdin.readline().strip())
case = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(5, 101):
    d[i] = d[i-1] + d[i-5]

for i in case:
    print(d[i])


# # 재귀함수 이용했을 경우.
# def triangle(T):
#     if T == 0:
#         result = 0
#     elif T == 1 or T == 2 or T == 3:
#         result = 1
#     elif T == 4:
#         result = 2
#     else:
#         result = triangle(T-1) + triangle(T-5)
#     return result

# for i in case:
#     print(triangle(i))