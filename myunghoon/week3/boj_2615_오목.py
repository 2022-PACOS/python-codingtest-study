def mapCheck(i, j) : 
    '''
    i,j 좌표가 map 안에 있으면 true, map 밖에 있으면 false를 반환한다.
    '''
    if (i >= 0 and i<=18) and (j >= 0 and j<=18) :
        return True
    else : 
        return False
def Checking(i,j) :
    '''
    i,j 좌표를 입력받아서 해당 좌표를 기준으로 오른쪽위, 오른쪽, 오른쪽아래, 아래쪽 총 4가지 방향으로 오목이 되는지 
    확인하고, 승부가 났으면 [1,[해당 좌표값]] 안됬으면 [0] 을 반환한다.
    '''
    # i,j좌표에서 오른쪽 위 방향
    if mapCheck(i-4,j+4) : 
        flag = True # 오목이면 True, 아니면 False
        for k in range(1,5) : 
            if board[i][j] != board[i-k][j+k] : 
                flag = False
        if mapCheck(i+1,j-1):
            if board[i][j] == board[i+1][j-1] :
                flag = False
        if mapCheck(i-5, j+5):
            if board[i][j] == board[i-5][j+5] :
                flag = False
        if flag==True : 
            return [board[i][j], [i,j]]
            
    # i,j좌표에서 오른쪽 방향
    if mapCheck(i,j+4) : 
        flag = True # 오목이면 True, 아니면 False
        for k in range(1,5) : 
            if board[i][j] != board[i][j+k] : 
                flag = False
        if mapCheck(i,j-1) : 
            if board[i][j] == board[i][j-1] : 
                flag = False
        if mapCheck(i,j+5) : 
            if board[i][j] == board[i][j+5] : 
                flag = False
        if flag == True :
           return [board[i][j],[i,j]]
        
    # i,j좌표에서 오른쪽 아래 방향
    if mapCheck(i+4,j+4) : 
        flag = True # 오목이면 True, 아니면 False
        for k in range(1,5) : 
            if board[i][j] != board[i+k][j+k] : 
                flag = False
        if mapCheck(i-1,j-1) : 
            if board[i][j] == board[i-1][j-1] : 
                flag = False
        if mapCheck(i+5, j+5): 
            if board[i][j] == board[i+5][j+5] : 
                flag = False
        if flag == True : 
           return [board[i][j],[i,j]]
    # i,j좌표에서 아래 방향
    if mapCheck(i+4,j) : 
        flag = True # 오목이면 True, 아니면 False
        for k in range(1,5) : 
            if board[i][j] != board[i+k][j] : 
                flag = False
        if mapCheck(i-1,j) :
            if board[i][j] == board[i-1][j] :
                flag = False
        if mapCheck(i+5,j) :
            if board[i][j] == board[i+5][j] :
                flag = False
        if flag == True :
            return [board[i][j],[i,j]]
    return [0]
board = []
result = [0]
isFind = 0
for i in range(19) :
    board.append(list(map(int,input().split())))

for i in range(19) : 
    if isFind == 1:
        break
    for j in range(19) : 
        if board[i][j] != 0 :
            result = Checking(i,j)
            if result[0] !=0 :
                print(result[0])
                print(result[1][0]+1, result[1][1]+1)
                isFind = 1
                break
if isFind == 0 :
    print(0)