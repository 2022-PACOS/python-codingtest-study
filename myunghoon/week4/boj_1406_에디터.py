import sys
myStr = input()
leftCursor = []
rightCursor = []

for i in myStr :
    leftCursor.append(i)

cmdCnt = int(sys.stdin.readline())
for i in range(cmdCnt) :
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'P' :
        leftCursor.append(cmd[1])
    elif cmd[0] == 'L' :
        if leftCursor : 
            rightCursor.append(leftCursor.pop())
    elif cmd[0] == 'D' :
        if rightCursor :
            leftCursor.append(rightCursor.pop())
    else :
        if leftCursor :
            leftCursor.pop()

while rightCursor :
    leftCursor.append(rightCursor.pop())
result = "".join(leftCursor)
print(result)