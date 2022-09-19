import sys
import copy
def solve(idx, s) :
    # 올바른 괄호 위치 배열에서 idx 번째를 제거하거나 혹은 제거하지 않는 2가지 경우를 만들어서 모든 조합 경우에 대해 answer에 추가한다.
    global pos_size
    if idx == pos_size : 
        myStr="".join(s)
        myStr = myStr.replace(" ","")
        answer.append(myStr)
    else :
        s2 = copy.deepcopy(s)
        s[pos[idx][0]] = " "
        s[pos[idx][1]] = " "
        solve(idx+1, s) # 제거 했을때
        solve(idx+1, s2) # 제거하지 않았을때

s = sys.stdin.readline().strip()
myStack = []
pos = [] #올바른 괄호의 위치를 담는 리스트
answer = [] #모든 괄호를 제거한 문자열을 담는 배열
for i in range(0, len(s)) :
    if (s[i] == '(') :
        myStack.append(i)
    elif (s[i] == ')') :
        pos.append([myStack.pop(),i])

pos_size = len(pos)
solve(0,list(s))

answer = set(answer)
answer.discard(s)
answer = list(answer)
answer.sort()

for elem in answer : 
    print(elem)