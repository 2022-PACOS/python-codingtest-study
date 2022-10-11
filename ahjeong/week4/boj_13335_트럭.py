from collections import deque

n, w, L = map(int, input().split(' '))
Truck = deque(list(map(int, input().split(' '))))

bridge = deque([0]*w)
total, result = 0, 0

while True:
    t = bridge.popleft()    # 현재 다리에 있는 트럭을 밖으로 이동.
    total -= t
    
    if Truck:    # 트럭 큐가 비워질 때 까지.
        if total + Truck[0] <= L:   # 현재 다리 위 무게 + 진입예정 트럭 무게 <= 최대하중
            bridge.append(Truck[0])
            total += Truck[0]
            Truck.popleft()
        else:   # 현재 다리 위 무게 + 진입예정 트럭 무게 > 최대하중, 트럭 잠시 대기하고 대신 0 추가
            bridge.append(0)
    result += 1 # 이동할 때 마다
    
    if not bridge:
        break

print(result)
