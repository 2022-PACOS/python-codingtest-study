import heapq

# 풀이1: 힙 2개 사용
def solution(operations):
    max_h = []
    min_h = []
    
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(max_h, -int(operations[i][2:]))
            heapq.heappush(min_h, int(operations[i][2:]))
        elif operations[i] == 'D 1':
            if len(max_h) !=0 and len(min_h) != 0:
                heapq.heappop(max_h)
                min_h = []
                for num in max_h:
                    heapq.heappush(min_h, -num)
            else:
                continue
        else:
            if len(max_h) !=0 and len(min_h) != 0:
                heapq.heappop(min_h)
                max_h = []
                for num in min_h:
                    heapq.heappush(max_h, -num)
            else:
                continue
    if len(max_h) !=0 and len(min_h) != 0:
        answer = [-max_h[0], min_h[0]]
    else:
        answer = [0,0]
            
    return answer

# 풀이 2: nlargest 사용
# import heapq

# def solution(operations):
#     h = []
#     for i in range(len(operations)):
#         if operations[i][0] == 'I':
#             heapq.heappush(h, int(operations[i][2:]))
#         elif operations[i] == 'D 1':
#             if len(h) !=0:
#                 h.pop(h.index(heapq.nlargest(1, h)[0]))   # heap에서 가장 큰 n개의 elements 
#             else:f
#                 continue
#         else:
#             if len(h) !=0:
#                 heapq.heappop(h)
#             else:
#                 continue
#     if len(h) !=0:
#         answer = [heapq.nlargest(1, h)[0], h[0]]
#     else:
#         answer = [0,0]
            
#     return answer