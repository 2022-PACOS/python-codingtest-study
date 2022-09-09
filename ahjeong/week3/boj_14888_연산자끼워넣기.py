from cmath import inf
import sys
from itertools import permutations
from collections import deque

N = int(input())
num = list(map(int, sys.stdin.readline().split(' ')))

opr = ['+', '-', '*', '//']
opr_input = list(map(int, sys.stdin.readline().split(' ')))
opr_list = []

# 사용가능한 연산자 리스트
for i in range(4):
    if opr_input[i] == 0:
        pass
    else:
        for j in range(opr_input[i]):
            opr_list.append(opr[i])

# 순열을 이용해 모든 경우의 수 생성
opr_case = list(permutations(opr_list, len(opr_list)))
q = deque(opr_case)

max_result = -inf
min_result = inf

while q:    # queue가 다 빌 때 까지
    now_cal = q.popleft()
    result = num[0]
    for i in range(1, len(num)):
        if now_cal[i-1] == '+':
            result += num[i]
        elif now_cal[i-1] == '-':
            result -= num[i]
        elif now_cal[i-1] == '*':
            result *= num[i]
        else:
            if result < 0:
                result = -(abs(result) // num[i])
            else:
                result = result // num[i]
            
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)