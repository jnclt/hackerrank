def is_prime(i):
    for j in range(2, i):
        if not i % j:
            return False
    return True

def primes():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

def waiter(number, q):
    prime_gen = primes()
    answers = []
    for i in range(q):
        prime = next(prime_gen)
        A, B = [], []
        while number:
            plate = number.pop()
            if plate % prime:
                A.append(plate)
            else:
                B.append(plate)
        answers.extend(reversed(B))
        number = A
    answers.extend(reversed(number))
    return answers