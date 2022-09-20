# https://www.acmicpc.net/problem/2800
# 백준 2800번 괄호 제거
# 메모리: 30840KB
# 시간: 116ms
# 코드길이: 914B
import sys
from itertools import combinations

n = list(sys.stdin.readline().strip())
print(n)

left = []
for i in range(len(n)):
    if n[i] == '(':
        left.append(i)
print("왼쪽 괄호 인덱스: ", left)

combi = []
for i in range(len(left)):
    for j in list(combinations(left, i + 1)):
        combi.append(list(j))
print("모든 조합: ", combi)

couple = []
temp = []
for i in range(len(n)):
    if n[i] == '(':
        temp.append(i)
    if n[i] == ')':
        couple.append((temp.pop(), i))
print("괄호 순서쌍: ", couple)

for i in range(len(combi)):
    temp = []
    for j in range(len(combi[i])):
        for k in couple:
            if k[0] == combi[i][j]:
                temp.append(k[0])
                temp.append(k[1])
    combi[i] = sorted(temp)
print("combi: ", combi)

answer = []
for i in combi:
    saved = []
    for index in range(len(n)):
        if index not in i:
            saved.append(n[index])
    if ''.join(saved) not in answer:
        answer.append(''.join(saved))

for i in sorted(answer):
    print(i)