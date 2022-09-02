import sys
# 바둑판 초기화
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(19)]

# 런타임 에러
# import sys
# # 바둑판 초기화
# matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(19)]

# def check(case, i, j):
#     for _ in range(5):
#         hori = case
#         if matrix[i][j] == matrix[i][j+1]:
#             hori.append([i, j+1])
#             j += 1
#         else:
#             break
#     for _ in range(5):
#         vert = case
#         if matrix[i][j] == matrix[i+1][j+1]:
#             vert.append([i+1, j+1])
#             i += 1
#             j += 1
#         else:
#             break
#     for _ in range(5):
#         diag = case
#         if matrix[i][j] == matrix[i+1][j]:
#             diag.append([i+1, j])
#             i += 1
#         else:
#             break
#     return max(hori, vert, diag) 

# def getResult():
#     case1 = []
#     case2 = []
#     for i in range(19):
#         for j in range(19):
#             if matrix[i][j] == 1:
#                 case = [[i, j]]
#                 case1 = check(case, i, j)
#             elif matrix[i][j] == 2:
#                 case = [[i, j]]
#                 case2 = check(case, i, j)
#             else:
#                 continue
#             # 검은색와 흰색이 동시에 이기는 경우가 없고 각각 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않음
#             if len(case1) == 5 or len(case2) == 5: 
#                 return case1, case2

# case1, case2 = getResult()

# if len(case1) == 5 and len(case2) != 5:
#     print(1)
#     i = case1[0][0] + 1
#     j = case1[0][1] + 1
#     print(i, j)
# elif len(case1) != 5 and len(case2) == 5:
#     print(2)
#     i = case2[0][0] + 1
#     j = case2[0][1] + 1
# else:
#     print(0)