import sys
N = int(sys.stdin.readline().strip())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*1001
d[1] = 1
d[2] = 3

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(3, 1001):
    d[i] = d[i-1] + d[i-2] * 2

print(d[N] % 10007)