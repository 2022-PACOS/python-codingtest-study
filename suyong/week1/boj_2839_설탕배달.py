import sys
answer = 0
n = int(sys.stdin.readline())

if n % 5 == 0:
    v = n // 5
    answer += v
elif n % 5 == 1:
    v = (n // 5) - 1 + 2
    answer += v
elif n % 5 == 2 and n != 7:
    v = (n // 5) - 2 + 4
    answer += v
elif n % 5 == 3:
    v = (n // 5) + 1
    answer += v
elif n % 5 == 4 and n != 4:
    v = (n // 5) - 1 + 3
    answer += v
else:
    answer = -1

print(answer)

