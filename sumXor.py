def sumXor(n):
    return 1 if not n else 2 ** format(n, 'b').count('0')