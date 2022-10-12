def solution(operations):
    import heapq

    answer = []

    minheap = []
    maxheap = []

    for op in operations:
        myop = op.split()
        action = myop[0]
        number = int(myop[1])
        print(op)
        if action == 'I':
            heapq.heappush(minheap, number)
            heapq.heappush(maxheap, (-number, number))
        elif action == 'D' and number == 1:
            if len(maxheap) > 0:
                maxv = heapq.heappop(maxheap)
                minheap.remove(maxv[1])
        elif action == 'D' and number == -1:
            if len(minheap) > 0:
                minv = heapq.heappop(minheap)
                for elem in maxheap:
                    if elem[1] == minv:
                        maxheap.remove(elem)
                        break

    if len(minheap) == 0 or len(maxheap) == 0:
        answer = [0, 0]
    else:
        answer = [heapq.heappop(maxheap)[1], heapq.heappop(minheap)]

    return answer