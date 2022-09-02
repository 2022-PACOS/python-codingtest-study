# https://www.acmicpc.net/problem/2615
# 백준 2615번 오목
# 메모리: 30840KB
# 시간: 72ms
# 코드길이: 9645B
import sys

array = []
for _ in range(19):
    k = sys.stdin.readline().strip().split(' ')
    array.append(k)
print("array: ", array)

answer = 0
x = 0
y = 0
logic = False
for i in range(len(array)):
    if logic:
        break
    for j in range(len(array[0])):
        print("좌표: ", (i, j))
        # 오른쪽으로(가로 흰색 승)
        if array[i][j] == '1' and j+4 < 19:
            if array[i][j+1] == '1' and array[i][j+2] == '1' and array[i][j+3] == '1' and array[i][j+4] == '1':
                if (0 <= i <= 18) and (1 <= j <= 13):
                    if array[i][j+5] != '1' and array[i][j-1] != '1':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 1
                        break
                elif j == 0:
                    if array[i][j+5] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif j == 14:
                    if array[i][j-1] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
        # 아래쪽으로(세로 흰색 승)
        if array[i][j] == '1' and i+4 < 19:
            if array[i+1][j] == '1' and array[i+2][j] == '1' and array[i+3][j] == '1' and array[i+4][j] == '1':
                if (1 <= i <= 13) and (0 <= j <= 18):
                    if array[i+5][j] != '1' and array[i-1][j] != '1':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 1
                        break
                elif i == 0:
                    if array[i+5][j] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif i == 14:
                    if array[i-1][j] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
        # 대각 5시쪽으로(대각 5시 흰색 승)
        if array[i][j] == '1' and i+4 < 19 and j+4 < 19:
            if array[i+1][j+1] == '1' and array[i+2][j+2] == '1' and array[i+3][j+3] == '1' and array[i+4][j+4] == '1':
                if j+5 <= 18 and j-1 >= 0 and i+5 <= 18 and i-1 >= 0:
                    if array[i+5][j+5] != '1' and array[i-1][j-1] != '1':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 1
                        break
                elif (j == 0 and i <= 13) or (i == 0 and j <= 13):
                    if array[i+5][j+5] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif (j == 14 and (1 <= i <= 14)) or (i == 14 and (1 <= j <= 14)):
                    if array[i-1][j-1] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif (i == 0 and j == 14) or (i == 14 and j == 0):
                    logic = True
                    x = i + 1
                    y = j + 1
                    answer = 1
                    break
        # 대각 1시쪽으로(대각 1시 흰색 승)
        if array[i][j] == '1' and i-4 >= 0 and j+4 < 19:
            if array[i-1][j+1] == '1' and array[i-2][j+2] == '1' and array[i-3][j+3] == '1' and array[i-4][j+4] == '1':
                if (5 <= i <= 17) and (1 <= j <= 13):
                    if array[i-5][j+5] != '1' and array[i+1][j-1] != '1':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 1
                        break
                elif (j == 0 and (5 <= i <= 18)) or (i == 18 and (0 <= j <= 13)):
                    if array[i-5][j+5] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif (i == 4 and (1 <= j <= 14)) or (j == 14 and (4 <= i <= 17)):
                    if array[i+1][j-1] != '1':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 1
                        break
                elif (i == 4 and j == 0) or (i == 18 and j == 14):
                    logic = True
                    x = i + 1
                    y = j + 1
                    answer = 1
                    break

        # 오른쪽으로(가로 검은색 승)
        if array[i][j] == '2' and j+4 < 19:
            if array[i][j+1] == '2' and array[i][j+2] == '2' and array[i][j+3] == '2' and array[i][j+4] == '2':
                if (0 <= i <= 18) and (1 <= j <= 13):
                    if array[i][j+5] != '2' and array[i][j-1] != '2':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 2
                        break
                elif j == 0:
                    if array[i][j+5] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif j == 14:
                    if array[i][j-1] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
        # 아래쪽으로(세로 검은색 승)
        if array[i][j] == '2' and i+4 < 19:
            if array[i+1][j] == '2' and array[i+2][j] == '2' and array[i+3][j] == '2' and array[i+4][j] == '2':
                if (1 <= i <= 13) and (0 <= j <= 18):
                    if array[i+5][j] != '2' and array[i-1][j] != '2':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 2
                        break
                elif i == 0:
                    if array[i+5][j] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif i == 14:
                    if array[i-1][j] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
        # 대각 5시쪽으로(대각 5시 검은색 승)
        if array[i][j] == '2' and i+4 < 19 and j+4 < 19:
            if array[i+1][j+1] == '2' and array[i+2][j+2] == '2' and array[i+3][j+3] == '2' and array[i+4][j+4] == '2':
                if j+5 <= 18 and j-1 >= 0 and i+5 <= 18 and i-1 >= 0:
                    if array[i+5][j+5] != '2' and array[i-1][j-1] != '2':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 2
                        break
                elif (j == 0 and i <= 13) or (i == 0 and j <= 13):
                    if array[i+5][j+5] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif (j == 14 and (1 <= i <= 14)) or (i == 14 and (1 <= j <= 14)):
                    if array[i-1][j-1] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif (i == 0 and j == 14) or (i == 14 and j == 0):
                    logic = True
                    x = i + 1
                    y = j + 1
                    answer = 2
                    break
        # 대각 1시쪽으로(대각 1시 검은색 승)
        if array[i][j] == '2' and i-4 > 0 and j+4 < 19:
            if array[i-1][j+1] == '2' and array[i-2][j+2] == '2' and array[i-3][j+3] == '2' and array[i-4][j+4] == '2':
                if (5 <= i <= 17) and (1 <= j <= 13):
                    if array[i-5][j+5] != '2' and array[i+1][j-1] != '2':
                        logic = True
                        x = i+1
                        y = j+1
                        answer = 2
                        break
                elif (j == 0 and (5 <= i <= 18)) or (i == 18 and (0 <= j <= 13)):
                    if array[i-5][j+5] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif (i == 4 and (1 <= j <= 14)) or (j == 14 and (4 <= i <= 17)):
                    if array[i+1][j-1] != '2':
                        logic = True
                        x = i + 1
                        y = j + 1
                        answer = 2
                        break
                elif (i == 4 and j == 0) or (i == 18 and j == 14):
                    logic = True
                    x = i + 1
                    y = j + 1
                    answer = 2
                    break

        if array[i][j] == '0':
            continue

print(answer)
if x != 0 and y != 0:
    print(x, y)




# # 모범답안
# # https://www.acmicpc.net/problem/2615
# # 백준 2615번 오목
# # 메모리: 30840KB
# # 시간: 72ms
# # 코드길이: 1217B
# import sys
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
# print(arr)
#
# dx = [1, 0, 1, -1]
# dy = [0, 1, 1, 1]
# answer = 0
#
# for i in range(19):
#     for j in range(19):
#         if arr[i][j]:
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 cnt = 1
#
#                 while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == arr[i][j]:
#                     cnt += 1
#                     if cnt == 5:
#                         # 뒤로 6목 판단
#                         if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and arr[nx + dx[k]][ny + dy[k]] == arr[i][j]:
#                             break
#                         # 앞으로 6목 판단
#                         if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and arr[i - dx[k]][j - dy[k]] == arr[i][j]:
#                             break
#                         # 6목 아니고 5목일시
#                         answer = arr[i][j]
#                         print(answer)
#                         print(i+1, j+1)
#                     nx += dx[k]
#                     ny += dy[k]
# if answer == 0:
#     print(0)
