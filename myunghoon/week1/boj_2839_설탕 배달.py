N = int(input())
answer = 0
fiveMax = N // 5
for i in range(fiveMax, -1, -1) :
    if (N-(5*i)) % 3 == 0 :
        answer = i+ ((N-(5*i)) // 3)
        break
if answer != 0 :
    print(answer)
else : 
    print(-1)