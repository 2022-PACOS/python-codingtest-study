
target = int(input())
n = int(input())
break_num= list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
    
        if int(nums[j]) in break_num:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)

# 1. 100번에서 +또는 - 해서 누른 횟수
# 2. 어떤 번호를 누른 후 + 또는 - 해서 누른 횟수

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 9]
# 만들 수 있는 숫자 중 5457과 가장 작은 차이가 나는 숫자?
# 이 방법의 문제점: 번호를 누르고 + 또는 - 버튼을 눌러 이동하는 횟수가 더 적을 수 있음, 시간초과

# from itertools import product

# channel = int(input())
# n = int(input())
# broken = list(map(int, input().split(' ')))
# remo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 고장난 번호 삭제
# for num in broken:
#     remo.remove(num)

# # 만들 수 있는 채널 경우의 수 
# case = []
# for i in range(1, len(remo)+1):
#     per = list(product(remo, repeat = i))
#     for j in per:
#         c = ''.join(map(str, j))
#         case.append(int(c))

# min_value = 1e9

# for c in case:
#     if 0 <= c <= 500000:
#         if abs(channel-c) < min_value:
#             min_value = abs(channel-c)
#             near = c
#             length = len(str(c))
#         else:
#             pass
#     else:
#         pass

# print(min_value)
# print(near)

# result = min(abs(100-channel), length+min_value)
# print(result)
