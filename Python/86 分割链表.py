"""
86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        frontList = ListNode(None)
        frontHead = frontList
        
        backList = ListNode(None)
        backHead = backList

        nowNode = head
        while nowNode != None:
            if nowNode.val < x:
                frontList.next = ListNode(nowNode.val)
                frontList = frontList.next
                #print("F:"+listNodeToString(frontHead))
            else:
                backList.next = ListNode(nowNode.val)
                backList = backList.next
                #print("B:"+listNodeToString(backHead))
            nowNode = nowNode.next
        frontList.next = backHead.next
        return frontHead.next