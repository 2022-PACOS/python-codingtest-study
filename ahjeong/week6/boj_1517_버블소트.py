# 코드와 해설 참고!
import sys

def devide(l,r) : 
    if l == r :
        return
    mid = (l + r)//2
    devide(l,mid)
    devide(mid+1,r)
    swap(l,mid,mid+1,r)
    return

def swap(ll,lr,rl,rr) :
    global swap_cnt
    temp_list = []
    start_idx = ll # 현재 temp_list의 위치를 알려주는 값
    si,li = ll,rr # start_index, last_index
    while ll <= lr and rl <= rr : #좌,우 배열 중 한쪽 배열이 temp_list에 다 들어갈 때까지 값을 비교
        if my_list[ll] > my_list[rl] : #오른쪽 배열에 있는 값을 temp_list로
            temp_list.append(my_list[rl])
            swap_cnt += (rl-start_idx)
            rl +=1 
            start_idx +=1 
        else :
            temp_list.append(my_list[ll])
            ll += 1
            start_idx += 1
    while ll <= lr : # 만약 왼쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[ll])
        ll +=1
    while rl <= rr : # 만약 오른쪽 배열이 temp_list로 덜 들어갔다면, 다 넣어준다.
        temp_list.append(my_list[rl])
        rl += 1
    for z in range(li,si-1,-1) : # temp_list에 넣어준 값을 하나씩 원래 배열로 넣어서 정렬시켜준다.
        my_list[z] = temp_list.pop()
    return


t = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
swap_cnt = 0
devide(0,len(my_list)-1)
print(swap_cnt)