import sys

answer = 0
array = []
n = int(sys.stdin.readline())
for i in range(n):
    array.append(list(map(int,sys.stdin.readline().split()))[0])
array.reverse()

for i in range(len(array) - 1):
    if array[i + 1] >= array[i]:
        answer = answer + (array[i + 1] - array[i] + 1)
        array[i + 1] = array[i] - 1

print(answer)
##