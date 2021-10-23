def decode_one(root, rs):
    if not (root.left and root.right):
        return root.data
    return decode_one(root.left if rs.popleft() == '0' else root.right, rs)
    
        
def decodeHuff(root, s):
    rest = deque(list(s))
    decoded = []
    while rest:
        decoded.append(decode_one(root, rest))
    print(''.join(decoded))