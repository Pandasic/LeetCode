#include "include.hpp"
using namespace std;
/*
题目描述
203. 移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
通过次数85,772提交次数187,658
*/

class Solution {
    public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* front = new ListNode(0);
        ListNode* rfront = front;
        front ->next = head;
        while(head != NULL)
        {
            if(head->val == val)
            {
                front ->next = head->next;
            }
            else
            {
                front = head;
            }
            head = head->next;
        }
        return rfront->next;
    }
};

class Solution {
    public:
    /*递归*/
    ListNode *removeElements(ListNode *head, int val)
    {
        if (!head)
            return head;
        head->next = removeElements(head->next, val);
        return head->val == val ? head->next : head;
    }
}
int main()
{
    Solution s;
    system("pause");
};