""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    if root is None:
        return True
    q = [(root, -10**100, 10**100)]
    while 0 < len(q):
        curr, min, max = q.pop()
        if curr.data < min or max < curr.data:
            return False
        if curr.left is not None:
            q.append((curr.left, min, curr.data-1))
        if curr.right is not None:
            q.append((curr.right, curr.data+1, max))
    return True
    
    
            