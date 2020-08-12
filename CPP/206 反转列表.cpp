#include "include.hpp"
using namespace std;
/*
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
*/

/*栈*/
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL)return NULL;

        stack <ListNode* > st;
        while(head->next!=NULL)
        {
            st.push(head);
            head=head->next;
        }
        ListNode * final=new ListNode(0);
        final=head;
        while (!st.empty())
        {
            head->next=st.top();
            st.pop();
            head=head->next;
        }
        head->next=NULL;
        return final;
    }
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL;
        while (head)
        {
            ListNode * temp = head->next;
            head->next = pre;
            pre = head;
            head = temp;
        }
        return pre;
    }
};


int main()
{
    Solution s;
    system("pause");
};