"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
通过次数22,176提交次数39,819
在真实的面试中遇到过这道题？
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#思路用双端队列完成
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        node = head
        while node != None:
            stack.append(node)
            node = node.next
        #q去掉头[就可以吃了 XD]
        stack = stack[1:]
        nowStat = False #True 为从头 False为末尾
        nowNode = head
        while len(stack) > 0:
            if not nowStat:
                temp = nowNode.next
                nowNode.next = stack.pop()
                nowNode = nowNode.next
                nowStat = not nowStat
            else:
                nowNode.next = stack.pop(0)
                nowNode = nowNode.next
                nowStat = not nowStat
        nowNode.next = None
        return head

#快慢指针 翻转后半段
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        fast, slow = head, head
        #找到中点
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        #反转后半链表
        p, right = slow.next, None
        slow.next = None
        while p:
            right, right.next, p = p, right, p.next
        #重排练表
        left = head
        while left and right:
            left.next,right.next,left,right = right,left.next,left.next,right.next

import tools         
s = Solution()
print(tools.listNodeToString(
s.reorderList(tools.stringToListNode("[1,2,3,4]"))))