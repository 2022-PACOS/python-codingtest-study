# # 왼쪽에 빈 열 2개를 추가하여 간단한 점화식으로 구현한 로직
# # https://www.acmicpc.net/problem/9465
# # 백준 9465번 스티커
# # 메모리: 50504KB
# # 시간: 1324ms
# # 코드길이: 547B
# import sys
# n = int(sys.stdin.readline())
# for _ in range(n):
#     array = []
#     m = int(sys.stdin.readline())
#     for _ in range(2):
#         nums = sys.stdin.readline().split(' ')
#         temp = [0, 0]
#         for j in range(m):
#             temp.append(int(nums[j]))
#         array.append(temp)
#     print(array)
#     for i in range(2, m + 2):
#         array[0][i] = max(array[1][i - 2] + array[0][i], array[1][i - 1] + array[0][i])
#         array[1][i] = max(array[0][i - 2] + array[1][i], array[0][i - 1] + array[1][i])
#     print(max(array[0][m+2-1], array[1][m+2-1]))


# 1열을 시작으로 1열, 2열을 따로 조건식으로 분리한 로직
# https://www.acmicpc.net/problem/9465
# 백준 9465번 스티커
# 메모리: 505044KB
# 시간: 1352ms
# 코드길이: 686B
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    array = []
    m = int(sys.stdin.readline())
    for _ in range(2):
        nums = sys.stdin.readline().split(' ')
        temp = []
        for j in range(m):
            temp.append(int(nums[j]))
        array.append(temp)
    print(array)
    for i in range(m):
        if i == 1:
            array[0][i] = array[1][i-1] + array[0][i]
            array[1][i] = array[0][i-1] + array[1][i]
        if i >= 2:
            array[0][i] = max(array[1][i - 2] + array[0][i], array[1][i - 1] + array[0][i])
            array[1][i] = max(array[0][i - 2] + array[1][i], array[0][i - 1] + array[1][i])
    print(max(array[0][m-1], array[1][m-1]))