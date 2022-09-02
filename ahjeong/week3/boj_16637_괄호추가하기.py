# import sys

# max_sum = float('-inf')
# input = sys.stdin.readline
# N = int(input())
# arr = input()
# num, operator = [], []

# # 연산자와 피연산자 배열을 구분함.
# def divide_num_operator(string, num, operator):
#     for i in string[:-1]:   
#         if i.isdigit():
#             num.append(int(i))
#         else:
#             operator.append(i)

# def calc(n1, n2, operator):
#     if operator == '*':
#         return n1 * n2
#     elif operator == '+':
#         return n1 + n2
#     elif operator == '-':
#         return n1 - n2

# # idx: 연산자의 인덱스
# # ret: 지금까지 계산된 결과
# # 식 앞에서부터 계산
# def dfs(idx, ret):
#     global max_sum
#     if idx >= len(operator):
#         max_sum = max(max_sum, ret)
#         return
 
#     # 이번에 계산 되는 경우
#     dfs(idx+1, calc(ret, num[idx+1], operator[idx]))
 
#     # 이번에 계산되지 않는 경우->뒤에가 먼저 계산되는 경우(괄호가 나보다 뒤에 있음)
#     if idx+1 < len(operator):
#         dfs(idx+2, calc(ret, calc(num[idx+1], num[idx+2], operator[idx+1]), operator[idx]))
 
# def solution(arr):
#     divide_num_operator(arr, num, operator)
 
#     dfs(0, num[0])

# solution(arr)
# print(max_sum)


from math import inf
from sys import stdin


def dfs(idx, sub_total):
    global answer

    if idx == len(op):
        answer = max(answer, int(sub_total))
        return

    # (3 + 8) * 7 - 9 * 2 부터 시작.
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + op[idx] + second))
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)


if __name__ == '__main__':
    n = int(stdin.readline())
    expression = stdin.readline().rstrip()
    nums, op = [], []
    answer = -inf

    for e in expression:
        nums.append(e) if e.isdigit() else op.append(e)

    dfs(0, nums[0])
    print(answer)