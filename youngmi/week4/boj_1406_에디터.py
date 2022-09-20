import sys
input = sys.stdin.readline

left = list(input().strip())
right = list()
m = int(input())
for i in range(m):
	c = input().split()
	if c[0] == 'L' and left :
		right.append(left.pop())
	elif c[0] == 'D' and right:
		left.append(right.pop())
	elif c[0] == 'B' and left:
		left.pop()
	elif c[0] == 'P': # else로 하면 런타임 에러
		left.append(c[1])

print(''.join(left + list(reversed(right))))