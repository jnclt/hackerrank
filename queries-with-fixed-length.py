# queries-with-fixed-length

def solve(arr, queries):
    answers = []
    for query in queries:
        maxes = []
        current_max = -1
        current_max_idx = -1
        for i in range(len(arr) - query + 1):
            if i > current_max_idx:
                current_max = max(arr[i:i + query])
                current_max_idx = i + arr[i:i + query].index(current_max)
            elif arr[i + query - 1] >= current_max:
                current_max = arr[i + query - 1]
                current_max_idx = i + query - 1
            maxes.append(current_max)
        answers.append(min(maxes))
    return answers