def arrayManipulation(n, queries):
    values = [0] * n
    for query in queries:
        for i in range(query[0] - 1, query[1]):
            values[i] += query[2]
    return max(values)