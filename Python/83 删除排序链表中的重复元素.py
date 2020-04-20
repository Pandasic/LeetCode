"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
通过次数84,579提交次数170,230

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        #当前节点
        nowNode = head
        #首节点
        beginNode = head
        while nowNode != None:
            if beginNode.val != nowNode.val :
                beginNode.next = nowNode
                beginNode = nowNode
            nowNode = nowNode.next
        beginNode.next = None
        return head