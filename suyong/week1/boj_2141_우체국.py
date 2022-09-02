import sys
n = int(sys.stdin.readline())
array = []
count = 0
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    count += end
    array.append([start, end])
array.sort()

temp = 0
for i in range(len(array)):
    temp += array[i][1]
    if temp >= round(count/2):
        print(array[i][0])
        break

##
