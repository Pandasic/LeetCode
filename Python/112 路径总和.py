"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""
import tools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return False
        def LDR (root,nowSum):
            if root == None:
                return False
            nowSum += root.val
            if root.left is None and root.right is None:
                if nowSum == sum:
                    return True
                else:
                    return False
            else:
                return LDR(root.left,nowSum) or LDR(root.right,nowSum)
        
        return LDR(root,0)

s = Solution()
tr = tools.stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
s.hasPathSum(tr,22)