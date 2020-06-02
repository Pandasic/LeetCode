"""
142. 环形链表 II
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


 

进阶：
你是否可以不用额外空间解决此题？

通过次数69,489提交次数139,445
在真实的面试中遇到过这道题？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
快慢双指针，先看是否能相遇，同141。
之后关键来了：相遇后，一个指针指向head，另一个不变。速度均改为1，继续移动、相遇。相遇点即是入环点。
具体的数学推导就不列举了。
"""
class Solution:
    def detectCycle(self, head):
        fast = head.next
        fastCount  = 1
        slow = head
        slowCount  = 0
        while fast != slow:
            if fast.next == None or fast.next.next == None:
                return -1
            fast = fast.next.next
            fastCount += 2
            slow = slow.next
            slowCount += 1
        return fastCount - slowCount