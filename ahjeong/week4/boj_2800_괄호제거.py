import sys
from itertools import combinations

s = list(sys.stdin.readline().rstrip())
left_b, right_b = [], []

for i, x in enumerate(s):
    if x == '(':
        left_b.append(i)    # 왼쪽 괄호 인덱스
    if x == ')':
        right_b.append((left_b.pop(), i))   # 왼쪽괄호, 오른쪽 괄호 인덱스

result = set()

for i in range(1, len(right_b) + 1):
    case = combinations(right_b, i)
    for j in case:
        tmp = s.copy()
        for l, r in j:
            tmp[l] = ''
            tmp[r] = ''
        result.add(''.join(tmp))

for i in sorted(result):
    print(i)