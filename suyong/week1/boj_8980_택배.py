from sys import stdin

N = int(stdin.readline())
villages = []
for _ in range(N):
    pos, peo = map(int, stdin.readline().split())
    villages.append([pos, peo])
print(villages)

distance = []
for pos in range(len(villages)):
    count = 0
    for peo in range(len(villages)):
        count += abs(villages[pos][0] - villages[peo][0]) * villages[peo][1]
    distance.append(count)

print(distance)

# from sys import stdin
#
# N = int(stdin.readline())
# villages = []
# for _ in range(N):
#     pos, peo = map(int, stdin.readline().split())
#     villages.append([pos, peo])
#
# distance = []
# for pos in range(len(villages)):
#     count = 0
#     for peo in range(len(villages)):
#         count += abs(villages[pos][0] - villages[peo][0]) * villages[peo][1]
#     distance.append(count)
#
# print(distance.index(min(distance))+1)
##dsds