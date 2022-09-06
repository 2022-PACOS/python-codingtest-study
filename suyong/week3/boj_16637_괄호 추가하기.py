# https://www.acmicpc.net/problem/16637
# 백준 16637번 괄호 추가하기
# 메모리: 실패
# 시간: 실패
# 코드길이: 실패
import sys
import math

n = int(sys.stdin.readline())
expression = sys.stdin.readline().rstrip()
nums, op = [], []
for e in expression:
    nums.append(e) if e.isdigit() else op.append(e)
answer = -math.inf


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


dfs(0, nums[0])
print(answer)