def maxMin(k, arr):
    print(len(arr))
    min_unfairness = 1_000_000_000
    arr.sort()
    print(arr)
    for i in range(len(arr) + 1 - k):
        unfairness = arr[i + k - 1] - arr[i]
        if unfairness < min_unfairness:
            min_unfairness = unfairness
    return min_unfairness