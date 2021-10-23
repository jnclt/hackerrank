def isValid(s):
    occurrences = {c: 0 for c in set(s)}
    for c in s:
        occurrences[c] += 1
    counts = list(occurrences.values())
    unique_counts = set(counts)
    if len(unique_counts) > 2:
        return 'NO'
    if len(unique_counts) == 1:
        return 'YES'
    count_A, count_B = list(unique_counts)
    if counts.count(count_A) > 1 and counts.count(count_B) > 1:
        return 'NO'
    if counts.count(count_A) == 1 and count_A > 1 and count_A != count_B + 1:
        return 'NO'
    if counts.count(count_B) == 1 and count_B > 1 and count_B != count_A + 1:
        return 'NO'
    return 'YES'