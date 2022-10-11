# 연산자 끼워놓기와 비슷한 문제
# dfs/bfs

k = int(input())
sign = list(map(str, input().split()))

# 방문
visitied = [False] * 11 
minResult, maxResult = "", ""

# 연산자
def possible(i, j, sign):
    if sign == '>':
        return i > j
    else:
        return i < j


def solve(depth, s):
    global minResult, maxResult

    if depth == k + 1:
        # 최솟값이 존재하지 않는다면, 최솟값으로 추가
        if len(minResult) == 0:
            minResult = s
        else:
            maxResult = s
        return

    for i in range(10):
        if not visitied[i]:
            if depth == 0 or possible(s[len(s) - 1], str(i), sign[depth - 1]):
                visitied[i] = True
                solve(depth + 1, s + str(i))
                visitied[i] = False


solve(0, "")

print(maxResult)
print(minResult)