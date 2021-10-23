# 6 out of 20 tests segfault, switch from recursion to iteration

sys.setrecursionlimit(100000)

def tree_sum(node, visited, neighbours, data, root_sum):
    if node in neighbours and neighbours[node] - visited:
        visited.add(node)
        sums, diffs = zip(*[tree_sum(succ, visited, neighbours, data, root_sum) for succ in neighbours[node] - visited])
    else:
        sums, diffs = [], []
    subtree_sum = sum(sums) + data[node - 1]
    subtree_min_diff = min(list(diffs) + [abs(root_sum - (2 * subtree_sum))])
    return (subtree_sum, subtree_min_diff)

def cutTheTree(data, edges):
    neighbours = {}
    for edge in edges:
        neighbours.setdefault(edge[0], set()).add(edge[1])
        neighbours.setdefault(edge[1], set()).add(edge[0])
    root_sum = sum(data)                
    return tree_sum(1, set(), neighbours, data, root_sum)[1]
