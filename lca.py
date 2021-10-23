def lca(root, v1, v2):
    def next_node(node, v):
        if v == node.info:
            return node
        elif v < node.info:
            return node.left
        else:
            return node.right
        
    common = next_1 = next_2 = root
    while True:
        next_1 = next_node(next_1, v1)
        next_2 = next_node(next_2, v2)
        if next_1 != next_2:
            return common
        common = next_1