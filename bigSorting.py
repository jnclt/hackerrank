def bigSorting(unsorted):
    lengths = {}
    for s in unsorted:
        lengths.setdefault(len(s), []).append(s)
    big_sorted = []
    for length in sorted(lengths.keys()):
        big_sorted.extend(sorted(lengths[length]))
    return big_sorted