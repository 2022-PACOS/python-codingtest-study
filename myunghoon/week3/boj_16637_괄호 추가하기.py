import math
def dfs(sub_result, nowDataIdx, nowOperIdx) :
    # sub_result:현재까지 계산된 결과, nowDataIdx:이제 계산을 할 대상 인덱스, nowoperIdx = 이제 계산을 할 연산 기호 인덱스
    global maxNum
    if nowDataIdx > len(data) -1 :
        if maxNum < sub_result :
            maxNum = sub_result
    else :
        if oper[nowOperIdx] == '+' :
            dfs(sub_result + data[nowDataIdx], nowDataIdx +1, nowOperIdx +1)
            if nowDataIdx + 1 <= len(data) - 1:
                if oper[nowOperIdx +1] == '+' :
                    dfs(sub_result + (data[nowDataIdx] + data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                elif oper[nowOperIdx +1] == '-' :
                    dfs(sub_result + (data[nowDataIdx] - data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                else : 
                    dfs(sub_result + (data[nowDataIdx] * data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
        elif oper[nowOperIdx] == '-' :
            dfs(sub_result - data[nowDataIdx], nowDataIdx +1, nowOperIdx +1)
            if nowDataIdx + 1 <= len(data) - 1:
                if oper[nowOperIdx +1] == '+' :
                    dfs(sub_result - (data[nowDataIdx] + data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                elif oper[nowOperIdx +1] == '-' :
                    dfs(sub_result - (data[nowDataIdx] - data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                else : 
                    dfs(sub_result - (data[nowDataIdx] * data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
        else :
            dfs(sub_result * data[nowDataIdx], nowDataIdx +1, nowOperIdx +1)            
            if nowDataIdx + 1 <= len(data) - 1:
                if oper[nowOperIdx +1] == '+' :
                    dfs(sub_result * (data[nowDataIdx] + data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                elif oper[nowOperIdx +1] == '-' :
                    dfs(sub_result * (data[nowDataIdx] - data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)
                else : 
                    dfs(sub_result * (data[nowDataIdx] * data[nowDataIdx + 1]), nowDataIdx + 2, nowOperIdx +2)     
N = int(input())
data = []
oper = []
number = []
str = list(input())
maxNum = -math.inf
for elem in str :
    if elem.isdigit() :
        number.append(elem)
    else :
        tmp=int(''.join(number))
        data.append(tmp)
        number.clear()
        oper.append(elem)
data.append(int(''.join(number)))

dfs(data[0], 1, 0)
print(maxNum)
