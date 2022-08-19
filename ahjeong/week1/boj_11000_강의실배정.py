import sys
N = int(sys.stdin.readline())
sbj = []
for i in range(N):
    sbj.append(list(map(int, sys.stdin.readline().strip().split(' '))))

room = [sbj[0][1]]      # 첫번째 원소
for i in range(1, N):
    for j in range(len(room)):
        print('j:',j)
        if  sbj[i][0] >= room[j]:
            room[j]= sbj[i][1]
            break
        else:
            print('sb: ',sbj[i][1])
            room.append(sbj[i][1])
             
print(room)