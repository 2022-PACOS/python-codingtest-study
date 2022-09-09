import sys

# 바둑판 초기화
matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(19)]

# (x, y) 현재 위치에서 오른쪽 위, 오른쪽, 오른쪽 아래, 아래 방향 
dir = [(-1, 1), (0, 1), (1, 1), (1, 0)]

def check(i, j):
    for d in dir:
        # 이동한 방향 좌표 구하기
        x, y = i + d[0], j+d[1]
        cnt = 1
        # 이동한 좌표의 범위 확인, 이동 전 좌표 == 이동 후 좌표 인지?
        while 0 <= x < 19 and y < 19 and matrix[x][y] == matrix[i][j]:
            cnt += 1
            x += d[0]
            y += d[1]
            if cnt == 5:
                # 오목이 완성 된 후 양쪽 끝에 같은 색의 바둑알이 있는지 확인 -> 6개 이상이 되는 것을 방지
                if not (0 <= x < 19 and y < 19 and matrix[x][y] == matrix[i][j]):
                    if not (0 <= i-d[0] < 19 and 0 <= j-d[1] < 19 and matrix[i-d[0]][j-d[1]] == matrix[i][j]):
                        print(matrix[i][j]) #이긴 바둑알의 번호를 출력
                        print(i+1, j+1)
                        exit(0)
                    else:
                        break
                else:
                    break

for i in range(19):
    for j in range(19):
        if matrix[i][j] != 0:
            check(i, j)

# check 함수에서 승부를 결정하지 않았을 경우 0을 출력함.
print(0)