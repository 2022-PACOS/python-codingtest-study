n = int(input())
k = int(input())

# s보다 작거나 같은 수의 개수 구하는 함수
def count(s):
    cnt = 0
    for i in range(1,n+1):
        cnt += min(s//i , n)
    return cnt

# 수의 범위 (1 ~ N x N)
start = 1
end = k # B[K](k번째 수)는 k보다 클 수 없다. B 배열을 그려보면 알 수 있음.
answer = 0

def binary_search(start,end,k):

    global answer
    if start > end: # 기저 조건
        answer = start
        return

    mid = (start + end) //2

    if count(mid) >= k:
        binary_search(start,mid-1,k)

    elif k > count(mid):
        binary_search(mid+1, end, k)

binary_search(start,end,k)

print(answer)