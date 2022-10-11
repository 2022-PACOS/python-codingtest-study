import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1
c_zero = abs(arr[start]+arr[end])
c_start = start
c_end = end

# 음수에서 양수로 넘어가는 부분까지
while start<end:
    tmp = arr[start]+arr[end]
    # tmp가 c_zero 보다 작다면 -> c_zero에 대입 / c_start,c_end 바꿈
    if abs(tmp) < c_zero:
        c_start = start
        c_end = end
        c_zero = abs(tmp)
        if c_zero == 0:
            break
    if tmp > 0:
        end -= 1
    else:
        start += 1

print(arr[c_start], arr[c_end])