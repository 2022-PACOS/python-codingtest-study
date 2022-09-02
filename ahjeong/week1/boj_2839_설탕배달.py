N = int(input())

rem = N % 5
quo = N // 5

if rem % 3 == 0:
    quo += rem // 3
elif quo > 0 and rem % 3 != 0:
    for i in range(1, quo+1):
        if (N-5*(quo-i)) % 3 == 0:
            quo += (N-5*(quo-i)) // 3 - i 
            break
        else:
            if i == quo:
                quo = -1
            continue
else:
    quo = -1
print(quo)