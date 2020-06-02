# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def LRD(root):
            if root == None:
                return
            LRD(root.left)
            LRD(root.right)
            res.append(root.val)
        LRD(root)
        return res
        