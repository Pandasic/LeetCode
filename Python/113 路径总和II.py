"""
113. 路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
通过次数40,021提交次数67,765

"""
import tools
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class mySolution:
    def pathSum(self, root: TreeNode, sum: int):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        res = []
        def LDR (root,nowSum,path):
            if root == None:
                return 
            nowSum += root.val
            path.append(root.val)
            if root.left is None and root.right is None:
                if nowSum == sum:
                    res.append(path)
            else:
                LDR(root.left,nowSum,path[:])
                LDR(root.right,nowSum,path[:])
        
        LDR(root,0,[])
        return res

#大佬思路 路径回溯 不用传递路径参数
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if root.left==None and root.right==None and root.val==sum:
            return [[root.val]]
        result=[]
        lefttree=self.pathSum(root.left,sum-root.val)
        righttree=self.pathSum(root.right,sum-root.val)
        for i in lefttree+righttree:
            result.append([root.val]+i)
        return result
s = Solution()
tr = tools.stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
print(s.pathSum(tr,22))