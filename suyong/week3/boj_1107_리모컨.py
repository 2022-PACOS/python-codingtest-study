# import sys
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# broken = list(map(int, sys.stdin.readline().split()))
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in broken:
#     nums.remove(i)
# print(nums)
#
# similar = []
# for i in list(map(int, str(n))):
#     sub = []
#     for j in nums:
#         if i-j < 0:
#         sub.append(abs(i - j))
#     print(sub)
#     print(min(sub))
#     location = list(filter(lambda x: sub[x] == min(sub), range(len(sub))))
#     print(location)
#     temp = []
#     for x in location:
#         temp.append(nums[x])
#     similar.append(temp)
# print(similar)
#
# answer = []
# result = []
#
#
# def dfs(index):
#     if len(result) == len(similar):
#         answer.append(int(''.join(map(str, result))))
#         return
#     else:
#         for a in similar[index]:
#             result.append(a)
#             dfs(index+1)
#             result.pop()
#
#
# dfs(0)
# print(answer)


# 모범답안
# https://www.acmicpc.net/problem/1107
# 백준 1107번 리모컨
# 메모리: 30840KB
# 시간: 1648ms
# 코드길이: 407B

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
answer = abs(100 - n)
broken = list(map(int, sys.stdin.readline().split()))
print(broken)

for i in range(1000000):
    logic = False
    for j in broken:
        if str(j) in list(str(i)):
            logic = True
            break
    if logic:
        continue
    else:
        answer = min(answer, len(list(str(i))) + abs(n - i))

print(answer)