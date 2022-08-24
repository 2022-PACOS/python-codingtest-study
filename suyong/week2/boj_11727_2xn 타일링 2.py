# https://www.acmicpc.net/problem/11727
# 해설: https://yongyongtv.tistory.com/17
# 백준 11727번 2xn 타일링
# 메모리: 실패
# 시간: 실패
# 코드길이: 227B

import sys
import math
n = int(sys.stdin.readline())
answer = 0

for i in range((n//2) + 1):
    temp = (math.factorial(n-i) // (math.factorial(n-2*i) * math.factorial(i))) * math.pow(2, i)
    answer += int(temp)
print(answer % 10007)


# # 모범답안
# table = [0, 1, 3]
#
# n = int(input())  # 입력값을 변수에 저장
# for i in range(3, n+1):
#     table.append(table[i-1] + 2*table[i-2])
#
# print(table[n] % 10007)  # n번째 index로 접근