"""
82. 删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
通过次数38,596提交次数82,352
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#统计然后构建
#当然也可以用递推法
#但是 有点想不明白 = = 
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = {}
        while head != None:
            if head.val in res.keys():
                res[head.val] += 1
            else:
                res[head.val] = 0
            head = head.next
        vals = []
        for v in res.keys():
            if res[v] < 1:
                vals.append(v)
        vals.sort()
        newHead = ListNode(None)
        now = newHead
        for v in vals:
            now.next = ListNode(v)
            now = now.next
        return newHead.next