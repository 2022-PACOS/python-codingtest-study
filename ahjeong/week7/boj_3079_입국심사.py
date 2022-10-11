# 해설 참고
# 다시 풀기
def solution(n, times):
    answer = 0
    start = 1
    # 가장 오래 걸리는 심사위원에게 모두 심사 받는 경우 
    end = max(times) * n
    while start <= end:
        people = 0 # 입국 심사 완료된 사람 수
        mid = (start + end) // 2 # mid 시간 동안 입국심사가 가능한지 판단
        for time in times:
            # 입국 심사가 가능한 사람 수
            people += mid//time

        # n 이상 심사 = mid로 가능하지만 더 가능할 수 있으니 
        # 일단 answer 에 저장하고 최소 mid 분 찾기
        if people >= n:
            answer = mid
            end = mid - 1
        # n보다 적은 수 심사
        else:
            start = mid + 1
    return answer