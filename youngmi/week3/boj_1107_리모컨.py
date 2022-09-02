import sys
input = sys.stdin.readline
target = int(input())
m = int(input()) # 고장난 번호 개수
broke = list(input().split()) # 고장난 번호들

move = abs(100-target) # 현재 채널에서 +,- 로 이동하는 경우 (절대값)

for num in range(1000001):
  for n in str(num): 
    if n in broke: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
      break
  else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
    move = min(move, len(str(num)) + abs(num - target))

print(move)