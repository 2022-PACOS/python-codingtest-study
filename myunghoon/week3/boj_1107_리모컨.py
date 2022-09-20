import sys
N = int(sys.stdin.readline()) # 이동하고자하는 채널
M = int(sys.stdin.readline()) # 고장난 개수
disabledNumbers = []
if M != 0:
    disabledNumbers = list(map(int, input().split()))
answer = abs(N-100)
end = 900001
if N == 100 : 
    answer = 0
else :
    for number in range(0,end) :
        flag = True
        numberList = list(map(int,list(str(number))))
        for num in numberList :
            if num in disabledNumbers : 
                flag = False 
                break
        if flag == True :
            answer = min(answer, (len(numberList) + abs(N-number)))

print(answer)