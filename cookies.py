def cookies(k, A):
    heapq.heapify(A)
    ops = 0
    while len(A) > 1 and A[0] < k:
        ops += 1
        least = heapq.heappop(A)
        second_least = heapq.heappop(A)
        new = (2 * second_least) + least
        heapq.heappush(A, new)
    if A[0] < k:
        return -1
    else:
        return ops