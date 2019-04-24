# Definition for a binary tree node.
import Queue
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.max_div = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.DLR(root,root.val,root.val)
        return self.max_div
        
    def DLR(self,node,nmax,nmin):
        if (node.val > nmax):
            nmax = node.val
        
        if (node.val < nmin):
            nmin = node.val

        if (nmax - nmin)>self.max_div:
            self.max_div = nmax - nmin

        if (node.left != None):
            self.DLR(node.left,nmax,nmin)

        if (node.right != None):
            self.DLR(node.right,nmax,nmin)
