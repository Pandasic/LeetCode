"""
148. 排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
通过次数57,861提交次数88,827

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 啊  看 一个勇士 用插排 冲了上去
# 哦 这个可怜的勇士 超时了 
import tools

#归并
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        # 快慢指针 分区
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        pre = slow.next
        slow.next = None
        
        #递归
        itorS = self.sortList(head)
        itorF = self.sortList(pre)

        if itorS == None:
            return itorF
        if itorF == None:
            return itorS

        #确定新的开始
        newHead = None
        if itorS.val > itorF.val:
            newHead = itorF
            itorF = itorF.next
        else:
            newHead = itorS
            itorS = itorS.next

        newNode = newHead
        while itorS != None and itorF != None:
            if itorS.val > itorF.val:
                newNode.next = itorF
                itorF = itorF.next
            else:
                newNode.next = itorS
                itorS = itorS.next
            newNode = newNode.next
        if itorF == None:
            newNode.next = itorS
        elif itorS == None:
            newNode.next = itorF
        return newHead

s = Solution()
res = (s.sortList(tools.stringToListNode("[-1,5,3,4,0]")))
print(tools.listNodeToString(res))
res = (s.sortList(tools.stringToListNode("[4,2,1,3]")))
print(tools.listNodeToString(res))