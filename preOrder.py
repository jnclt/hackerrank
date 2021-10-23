def preOrder(root):
    if not root:
        return
    print(f'{root.info}', end=' ')
    preOrder(root.left)
    preOrder(root.right)