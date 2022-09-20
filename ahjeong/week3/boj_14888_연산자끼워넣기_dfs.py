from cmath import inf

N = int(input())
num = list(map(int,input().split(' ')))
add, sub, mul, div = map(int, input().split(' '))

max_value = -inf
min_value = inf

# DFS 탐색
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == N:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/num[i]))   # 음수를 양수로 나눌 때
            div += 1

dfs(1, num[0])

print(max_value)
print(min_value)