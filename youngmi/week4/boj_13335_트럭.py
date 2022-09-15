import sys

input = sys.stdin.readline
n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 다리 하중
trucks = list(map(int, input().split()))

bridge = [0] * w # 다리의 칸
times = 0

# 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
while bridge:
	bridge.pop(0) # 다리 앞쪽 삭제
	times += 1 # 시간 증가

	# 지나가야하는 트럭이 있다면
	if trucks:
		# 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가
   		# 다리의 하중보다 작다면 트럭을 다리에 추가
		if sum(bridge) + trucks[0] <= l:
			bridge.append(trucks.pop(0))
		# 다리의 하중보다 크다면 빈 공간을 추가
		else:
			bridge.append(0)
		
print(times)