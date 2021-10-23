def add(digits, digit):
    if not digits:
        return [digit]
    sum = digits[0] + digit
    digits[0] = sum % 10
    if sum < 10:
        return digits
    return [digits[0]] + add(digits[1:], 1)
    
def reduce(digits):
    reduced = []
    for digit in digits:
        reduced = add(reduced, digit)
    return reduced
    
def super_digit_base(digits):
    if len(digits) == 1:
        return digits[0]
    return super_digit_base(reduce(digits))
    
def superDigit(n, k):
    digits = str(super_digit_base(list(map(int, list(n)))*k))
    return super_digit_base(list(map(int, list(digits))))