def counts(s):
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

def anagram(s):
    if len(s) % 2:
        return -1
    split = len(s) // 2
    left = counts(s[:split])
    right = counts(s[split:])
    for c in left:
        if c in right:
            lower = min(left[c], right[c])
            left[c] -= lower
            right[c] -= lower
    delta_left = sum(left.values())
    delta_right = sum(right.values())
    if delta_left != delta_right:
        return -1
    return delta_left
