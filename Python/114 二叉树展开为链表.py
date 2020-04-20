"""
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
通过次数34,771提交次数50,931
"""
import tools
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#展开对了 但是顺序不对 而且烦 == 
class mySolution:
    def flatten(self, root) -> None:
        if not root:
            return None
        #寻找最右的节点
        if root.left != None and root.right == None:
            root.right = root.left
            root.left = None
            return self.flatten(root.right)
        elif root.right == None:
            return root
        rightestNode = self.flatten(root.right)
        print(rightestNode.val)
        if root.left != None:
            rightestNode.right = root.left
            root.left = None
            return self.flatten(rightestNode.right)
        else:
            return rightestNode

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root or (not root.left and not root.right):
            return root
        
        #先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right #把捋直的右子树备份一下
        
        root.right = root.left #把捋直的左子树放到右边
        root.left = None #记得把左子树置空
        while(root.right): #找到现在右子树的最后一个node
            root = root.right
        root.right = tmp #把捋直的原来的右子树接上去

s = Solution()
tr = tools.stringToTreeNode("[1,2,5,3,4,null,6]")
print(s.flatten(tr))