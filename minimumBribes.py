def minimumBribes(q):
    bribes = 0
    reference = list(range(1, len(q) + 1))
    for i, p in enumerate(q):
        if p > i + 3:
            print("Too chaotic")
            return
        bribes_p = reference.index(p)
        reference.pop(bribes_p)
        bribes += bribes_p
    print(bribes)

            