# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class IsSubtree():
    def identicalTree(self, root, otherRoot):
        if not root and not otherRoot:
            return True
        if not root or not otherRoot:
            return False
        return root.val == otherRoot.val and self.identicalTree(root.left, otherRoot.left) and self.identicalTree(root.right, otherRoot.right)
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val and self.identicalTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        