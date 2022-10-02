# 총 합계를 기준으로 봤을 때, i 번째 요소가 n -i번 더해지니까 ` (n-i) * p[i]`로도 풀 수 있다.
# 실행 시간과 메모리 사용량은 첫번째 풀이와 동일하다. 장점은 코드 길이가 조금 짧아진다는것 정도,,?

n = int(input())
p = list(map(int,input().split()))
p.sort()
time = 0

for i in range(n):
    time += (n-i) * p[i]
    
print(time)