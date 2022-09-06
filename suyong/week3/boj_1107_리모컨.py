# https://www.acmicpc.net/problem/1107
# 백준 1107번 리모컨
# 메모리: 실패
# 시간: 실패
# 코드길이: 1710B
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))
able = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in broken:
    able.remove(i)
print("able: ", able)

atom = list(map(int, list(str(n))))
print("atom: ", atom)

result1 = []
result2 = []
for k in atom:
    diff = []
    for a in able:
        diff.append(abs(k-a))
    print("diff: ", diff)

    if k in able:
        result1.append(k)
        result2.append(k)
    else:
        num = []
        for j in list(filter(lambda x: diff[x] == min(diff), range(len(diff)))):
            num.append(able[j])
        print("num: ", num)
        if len(num) == 1:
            if num[0] > k:
                result1.append(num[0])
                result2.append(num[0])
                for _ in range(len(atom) - len(result1)):
                    result1.append(able[0])
                for _ in range(len(atom) - len(result2)):
                    result2.append(able[0])
                break
            else:
                result1.append(num[0])
                result2.append(num[0])
                for _ in range(len(atom) - len(result1)):
                    result1.append(able[-1])
                for _ in range(len(atom) - len(result2)):
                    result2.append(able[-1])
                break
        else:
            result1.append(num[0])
            result2.append(num[1])
            for _ in range(len(atom) - len(result1)):
                result1.append(able[-1])
            for _ in range(len(atom) - len(result2)):
                result2.append(able[0])
            break
    print("---------------")
result1 = int(''.join(list(map(str, result1))))
result2 = int(''.join(list(map(str, result2))))
print("result1: ", result1)
print("result2: ", result2)

answer = min(abs(100 - n), min(abs(n-result1), abs(n-result2)) + len(atom))
print(answer)

a = [1,2,3,4,5]
print(int(''.join(list(map(str,a)))))



# 모범답안
# https://www.acmicpc.net/problem/1107
# 백준 1107번 리모컨
# 메모리: 30840KB
# 시간: 1648ms
# 코드길이: 407B

# import sys
#
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# answer = abs(100 - n)
# broken = list(map(int, sys.stdin.readline().split()))
#
# for i in range(1000000):
#     logic = False
#     for j in broken:
#         if str(j) in list(str(i)):
#             logic = True
#             break
#     if logic:
#         continue
#     else:
#         answer = min(answer, len(list(str(i))) + abs(n - i))
#
# print(answer)