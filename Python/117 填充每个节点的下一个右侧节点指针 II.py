"""
117. 填充每个节点的下一个右侧节点指针 II
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        preNode = None
        if root.left is not None:
            if root.right is not None:
                root.left.next = root.right
                preNode = root.right
            else:
                preNode = root.left
        elif root.right is not None:
            preNode = root.right
        else:
            return root

        if preNode is None:
            return

        nextNode = root.next
        while(nextNode != None):
            if root.next.left != None:
                preNode.next = root.next.left
                break
            elif root.next.right != None:
                preNode.next = root.next.right
                break
            else:
                nextNode = nextNode.next

        self.connect(root.left)
        self.connect(root.right)
        return root