# https://www.acmicpc.net/problem/14888
# 백준 14888번 연산자 끼워넣기
# 메모리: 524856KB
# 시간: 3320ms
# 코드길이: 1182B
import sys
from itertools import permutations


n = int(sys.stdin.readline())
nums = []
temp = sys.stdin.readline().split()
for i in range(n):
    nums.append(int(temp[i]))
op = []
temp = sys.stdin.readline().split()
for i in range(len(temp)):
    op.append(int(temp[i]))

per_tot = 0
for i in op:
    per_tot += i

ops = []
for i in range(len(op)):
    if i == 0:
        for j in range(op[i]):
            ops.append('+')
    elif i == 1:
        for j in range(op[i]):
            ops.append('-')
    elif i == 2:
        for j in range(op[i]):
            ops.append('*')
    else:
        for j in range(op[i]):
            ops.append('//')

solve = []
for i in permutations(ops, per_tot):
    solve.append(i)

a = list(set(solve))
print(a)

result = []
for i in a:
    strings = str(nums[0])
    for j in range(len(i)):
        if int(strings) < 0 and i[j] == "//":
            string_temp = i[j] + str(nums[j+1])
            strings = str(-(abs((int(strings))) // nums[j+1]))
        else:
            string_temp = i[j] + str(nums[j+1])
            strings += string_temp
            strings = str(eval(strings))
    print(strings)
    result.append(int(strings))

print(max(result))
print(min(result))