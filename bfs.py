def bfs(n, m, edges, s):
    print(f'n: {n}, m: {m}, s: {s}')
    distances = [-1] * (n + 1)
    edges = set([(e[0], e[1]) for e in edges])
    level = set([s])
    next_level = set()
    level_idx = 1
    while level:
        print(level)
        for node in level:
            processed = set()
            for edge in edges:
                if node in edge:
                    succ = edge[1 - edge.index(node)]
                    next_level.add(succ)
                    if distances[succ] == -1:
                        distances[succ] = 6 * level_idx
                    processed.add(edge)
            edges -= processed
            processed.clear()
        level_idx += 1
        level = next_level
        next_level = set()
    return distances[1:s] + distances[(s + 1):]


# incorrect
WEIGHT = 6

def bfs(n, m, edges, s):
    neighbours = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        neighbours[edge[0]].add(edge[1])
        neighbours[edge[1]].add(edge[0])
    
    distances = {i: -1 for i in range(1, n + 1)}
    current_level = set([s])
    next_level = set()
    visited = set()
    distance = 0
    while current_level:
        node = current_level.pop()
        distances[node] = distance
        visited.add(node)
        next_level |= (neighbours[node] - visited)
        if not current_level:
            distance += WEIGHT
            current_level = next_level
            next_level = set()

    return [distances[i] for i in range(1, n + 1) if i != s]