# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归
class mySolution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.part(root)
        return self.res

    def part(self, root: TreeNode):
        if root == None:
            return
        self.part(root.left)
        self.res.append(root.val)
        self.part(root.right)

#迭代
#迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        stack, ret = [], []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret