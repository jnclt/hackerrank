import heapq

def count_swaps(arr):
    indices, values = {}, {}
    for i, v in enumerate(arr):
        indices[v] = i
        values[i] = v
    heapq.heapify(arr)
    swaps = 0
    idx = 0
    while arr:
        lowest = heapq.heappop(arr)
        if indices[lowest] != idx:
            swaps += 1
            indices[values[idx]] = indices[lowest]
            values[indices[lowest]] = values[idx]
            indices[lowest] = idx
        idx += 1
    return swaps

def lilysHomework(arr):
    swaps_asc = count_swaps(arr.copy())
    highest = max(arr)
    arr = [highest - v for v in arr]
    swaps_desc = count_swaps(arr)

    return min(swaps_asc, swaps_desc)