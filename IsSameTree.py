class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class IsSameTree():
    def isSameTree(self, p, q):
        if p.val != q.val:
            return False
        