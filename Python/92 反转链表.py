"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
import tools

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m - 1):
            pre = pre.next
        head = pre.next
        for i in range(m,n):
            nex = head.next
            head.next = nex.next
            nex.next = pre.next
            pre.next = nex
            #print(tools.listNodeToString(dummy))
        return dummy.next

s = Solution()
head = tools.stringToListNode("[1,2,3,4,5]")
head = s.reverseBetween(head,2,4)
print(tools.listNodeToString(head))