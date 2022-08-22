import sys
weight = sys.stdin.readline().split(' ')
array = []
n = int(weight[0])
m = int(weight[1])
for _ in range(n):
    nums = sys.stdin.readline().strip()
    temp = []
    for i in str(nums):
        temp.append(int(i))
    array.append(temp)



print(array)