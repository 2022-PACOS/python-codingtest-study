import sys
from itertools import combinations

n = list(map(str, sys.stdin.readline().strip()))
answer = set()
stack, pos = [], []

for idx, word in enumerate(n):
    if word == '(':
        stack.append(idx)
    elif word == ')':
        pos.append((stack.pop(), idx)) # 괄호의 시작점과 끝점 저장

for i in range(1, len(pos) + 1):
    c = combinations(pos, i) # combinations을 통해 모든 경우의 수를 확인

    # 반복문을 통해 경우의 수를 확인
    for j in c:
        temp = list(n)
        # 괄호 제거
        for s, e in j:
            temp[s] = ''
            temp[e] = ''
        answer.add(''.join(temp))

for ans in sorted(list(answer)):
    print(ans)