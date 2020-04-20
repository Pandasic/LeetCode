# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #想法 广度优先遍历
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False

            if left.val == right.val:
                res = True
                res &= isMirror(left.left,right.right)
                res &= isMirror(left.right,right.left)
                return res
            else:
                return False
        
        if root is None:
            return True
        return isMirror(root.left,root.right)