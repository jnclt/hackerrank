def lcm(a, limit):
    x = step = max(a)
    while any(map(lambda y: x % y, a)) and x <= limit - step:
        x += step
    if any(map(lambda y: x % y, a)):
        return 0
    return x

def getTotalX(a, b):
    limit = min(b)
    candidate = step = lcm(a, limit)
    if candidate == 0:
        return 0
    count = 0
    while candidate <= limit:
        if not any(map(lambda x: x % candidate, b)):
            count += 1
        candidate += step
    return count