from itertools import permutations

k = int(input())
signs = input().split()

result = []
for num in permutations([0,1,2,3,4,5,6,7,8,9],k+1) :
  for i in range(len(signs)) :
    if signs[i] == '<' :
      if not num[i] < num[i+1] : 
        break
    else :
      if not num[i] > num[i+1] :
        break
  else:
    result.append(num)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))