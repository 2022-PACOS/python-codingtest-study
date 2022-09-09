N = int(input())
data = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())
maxNum = -10000000000
minNum = 10000000000
def calc(plus,minus,mul,div, res, idx) :
# 주어진 연산 횟수에서 발생한 모든 경우에 대해 연산한 결과의 
# 최대값(maxNum),최소값(minNum)을 갱신한다.
 global maxNum
 global minNum
 if idx == N-1 :
    if res > maxNum :
        maxNum = res
    if res < minNum :
        minNum = res
    return
 if plus > 0 :
    calc(plus-1,minus,mul,div, res + data[idx+1], idx+1)
 if minus > 0 :
    calc(plus,minus-1,mul,div,res - data[idx+1], idx+1)
 if mul > 0 :
    calc(plus,minus,mul-1,div, res * data[idx+1], idx+1)
 if div > 0 :
    calc(plus,minus,mul,div-1, int(res/data[idx+1]), idx+1)

calc(plus,minus,mul,div,data[0], 0)
print(maxNum)
print(minNum)
