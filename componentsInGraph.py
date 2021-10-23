from queue import deque

def componentsInGraph(gb):
    neighbours = {}
    for edge in gb:
        neighbours.setdefault(edge[0], set()).add(edge[1])
        neighbours.setdefault(edge[1], set()).add(edge[0])

    components = []
    to_visit = set(neighbours.keys())
    while to_visit:
        nodes = deque([to_visit.pop()])
        component = set()
        while nodes:
            node = nodes.popleft()
            component.add(node)
            to_visit.discard(node)
            nodes.extend(neighbours[node] & to_visit)
        components.append(component)
    
    sizes = [len(component) for component in components]
    return [min(sizes), max(sizes)]