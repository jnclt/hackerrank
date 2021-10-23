def decodeHuff(root, s):
    decoded = ""
    node = root
    for code in s:
        node = node.right if int(code) else node.left
        if node.left is None and node.right is None:
            decoded += node.data
            node = root
    print(decoded)