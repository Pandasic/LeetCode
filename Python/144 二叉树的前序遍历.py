# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def LDR(node):
            if root == None:
                return
            res.append(root.val)
            LDR(root.left)
            LDR(root.right)
        LDR(root)
        return res
        