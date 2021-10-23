MOD = 1_000_000_007

def get_rows(m):
    rows = [1, 1, 2, 4, 8]
    for i in range(len(rows), m + 1):
        rows.append(sum(rows[-4:]) % MOD)
    return rows
    
def legoBlocks(n, m):
    rows = get_rows(m)
    all_stacks = [pow(row, n, MOD) for row in rows]
    unstable_stacks = [0, 0]
    for i in range(2, m + 1):
        unstable_stacks.append(0)
        for j in range(1, i):
            unstable_stacks[i] += (all_stacks[j] - unstable_stacks[j]) * all_stacks[i - j]       
        unstable_stacks[i] = unstable_stacks[i] % MOD
    return (all_stacks[m] - unstable_stacks[m]) % MOD
