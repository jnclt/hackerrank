def pairs(k, arr):
    values = {}
    for v in arr:
        values[v] = values.setdefault(v, 0) + 1
    pairs = 0
    for v, count in values.items():
        if (v + k) in values:
            pairs += count
    return pairs