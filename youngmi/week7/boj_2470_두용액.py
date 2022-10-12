# 투포인터 문제
n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left, right = 0, n-1
mix = abs(solutions[left] + solutions[right])
answer = [solutions[left], solutions[right]]

while left < right:
	left_s, right_s = solutions[left], solutions[right]

	temp_mix = left_s + right_s
	if abs(temp_mix) < mix:
		mix = abs(temp_mix) 
		answer = [left_s, right_s]
		if mix == 0:
			break
	if temp_mix < 0:
		left += 1
	else:
		right -= 1

print(answer[0], answer[1])