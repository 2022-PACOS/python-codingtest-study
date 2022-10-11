def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()  # 징검다리 정렬
    rocks.append(distance)
    
    left, right = 0, distance
    
    # 이진 탐색
    while left <= right:
        # N개 바위를 제거했을 때 바위 사이의 간격 최소 거리: mid 라고 가정
        mid = (left + right) // 2  
        min_distance = float('inf')  # 각 mid 에서 최솟값
        current = 0  # 현재 위치
        remove_cnt = 0  # 바위를 제거한 개수
        
        # 바위에서 거리 구하기
        for rock in rocks:
            diff = rock - current  # 바위와 현재 위치 사이의 거리
            if diff < mid:  # mid 보다 거리가 짧으면 바위 제거
                remove_cnt += 1
            else:  # mid 보다 거리가 길거나 같으면 바위 그대로 두고
                current = rock  # 현재 위치를 그 바위로 옮기기,이 이후는 어차피 diff>mid 이므로.
                min_distance = min(min_distance, diff)  # 해당 mid 단계에서의 최소거리인지 체크
        
        # mid를 설정하는 단계
        if remove_cnt > n:  # 바위를 너무 많이 제거 -> mid를 줄여서 바위를 조금만 제거
            right = mid - 1
        else:  # 바위를 너무 적게 제거 또는 알맞게 제거 -> mid를 늘려서 바위를 더 제거
            answer = min_distance
            left = mid + 1

    return answer