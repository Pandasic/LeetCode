"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
通过次数98,842提交次数161,084
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#中序遍历
class LDR_Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = {}

        def LDR (root,depth):
            if root == None:
                return
            if depth not in res.keys():
                res[depth] = root.val
            else:
                res[depth].append(root.val)
            LDR(root.left,depth + 1)
            LDR(root.right,depth + 1)
        
        LDR(root,0)
        return res.values

class BFS_Solution(object):
    def levelOrder(self, root):
        Queue = [(root,0)]
        res = []
        while len(Queue) > 0:
            node,depth = Queue[0]
            Queue = Queue[1:]
            
            if node == None:
                continue
            
            if len(res) <= depth:
                res.append([])
            res[depth].append(node.val)
            Queue.append((node.left,depth + 1))
            Queue.append((node.right,depth + 1))
        return res