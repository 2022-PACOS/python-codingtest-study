import sys
import copy

n = int(sys.stdin.readline())

expression = sys.stdin.readline().rstrip()
nums, op = [], []
for e in expression:
    nums.append(e) if e.isdigit() else op.append(e)
print("nums: ", nums)
print("op: ", op)


for i in range(len(nums)-1):
    a = copy.deepcopy(nums)
    a[i] = '(' + a[i]
    a[i+1] = a[i+1] + ')'

