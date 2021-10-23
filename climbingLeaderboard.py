def climbingLeaderboard(ranked, player):
    ranks = []
    scores = set(ranked)
    for score in player:
        scores.add(score)
        ranks.append(sorted(scores, reverse=True).index(score) + 1)
    return ranks

########################
def climbingLeaderboard(ranked, player):
    ranks = []
    current_rank = 1
    for i in range(1, len(ranked)):
        if ranked[i] != ranked[i - 1]:
            current_rank += 1
    current_idx = len(ranked) - 1
    
    for score in player:
        while current_idx > 0 and score >= ranked[current_idx]:
            while current_idx > 0 and (ranked[current_idx] == ranked[current_idx - 1]):
                current_idx -= 1
            current_rank -= 1
            current_idx -= 1
        print(current_rank, current_idx)
        ranks.append(current_rank + 1 if current_idx > 0 else 1)
        
    return ranks

########################

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'({self.value}: {self.left} / {self.right})'

def climbingLeaderboard(ranked, player):
    def build_tree(scores):
        if not scores:
            return None
        mid = len(scores) // 2
        return Node(scores[mid], build_tree(scores[:mid]), build_tree(scores[mid + 1:]))
    
    def insert(score, root):
        if root.value == score:
            return
        elif root.value > score:
            if not root.left:
                root.left = Node(score, None, None)
            else:
                insert(score, root.left)
        else:
            if not root.right:
                root.right = Node(score, None, None)
            else:
                insert(score, root.right)

    def index(node, value):
        if node.value == value:
            return 0 if not node.right else tree_size(node.right)
        elif node.value < value:
            return index(node.right, value)
        else:
            size_right = 0 if not node.right else tree_size(node.right)
            return size_right + 1 + index(node.left, value)
    
    def tree_size(node):
        left = 0 if not node.left else tree_size(node.left)
        right = 0 if not node.right else tree_size(node.right)
        return 1 + left + right
        
    scores = sorted(set(ranked))
    tree = build_tree(scores)
    # print(tree)
    orders = []
    for score in player:
        insert(score, tree)
        # print(tree)
        orders.append(index(tree, score) + 1)
    return orders