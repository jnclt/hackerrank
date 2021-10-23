def twoArrays(k, A, B):
    B.sort(reverse=True)
    A.sort()
    below_k = list(filter(lambda x: x < k, A))
    while B and below_k:
        lowest = B.pop()
        highest_short = below_k.pop()
        while highest_short + lowest < k:
            if not B:
                return 'NO'
            lowest = B.pop()
    if below_k:
        return('NO')
    return 'YES'