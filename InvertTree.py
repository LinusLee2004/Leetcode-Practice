# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class InvertTree():
    def invertTree(self, root):
        if not root:
            return None
        leftSide = root.left
        rightSide = root.right
        root.left = rightSide
        root.right = leftSide
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
