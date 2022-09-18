from collections import deque
n, bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))

answer = 0
bridge = deque([0]*bridge_length) # [0,0]
complete = []
truck_length = len(truck_weights)
truck_weights.reverse()
total_weight = 0 
while len(complete) <  truck_length:
    tmp = bridge.popleft()
    total_weight -= tmp
    if tmp > 0 :
        complete.append(tmp)

    if truck_weights:
        if (total_weight + truck_weights[-1]) <= weight :
            bridge.append(truck_weights[-1])
            total_weight += truck_weights[-1]
            truck_weights.pop()
        else : 
            bridge.append(0)
    answer += 1

print(answer)