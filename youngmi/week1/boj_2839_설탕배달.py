# https://www.acmicpc.net/problem/2839
# 백준 2839번 설탕배달
# 메모리: 30840KB
# 시간: 68ms
# 코드길이: 238B

n = int(input())
total = -1

if n % 5 == 0:
    total = n // 5
else:
    for i in reversed(range(n//5+1)):
        if (n - (i*5)) % 3 == 0:
            three = (n - (i*5)) // 3
            total = i + three
            break

print(total)
``