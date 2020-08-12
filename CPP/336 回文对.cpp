#include "include.hpp"
using namespace std;
/*
336. 回文对
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

 

示例 1：

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]] 
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]] 
解释：可拼接成的回文串为 ["battab","tabbat"]
*/

/*暴力法 遍历*/
class Solution {
public:
    bool isPalindrome(string str)
    {
        string temp = str;
        reverse(str.begin(),str.end());
        return temp == str;
    }
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> res;
        for(int i = 0; i < words.size() - 1 ;i++)
        {
            for(int j = i + 1;j < words.size(); j++)
            {
                if(isPalindrome(words[i] + words[j]))
                    res.push_back(vector<int>{i,j});
                if(isPalindrome(words[j] + words[i]))
                    res.push_back(vector<int>{j,i});
            }
        }
        return res;
    }
};

/*哈希*/
class Solution {
public:
    bool isPalindrome(string str)
    {
        string temp = str;
        reverse(str.begin(),str.end());
        return temp == str;
    }
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> b(26),e(26);
        vector<vector<int>> res;
        int emptyIndex = -1;
        for(int i = 0;i< words.size();i++)
        {
            string& w = words[i];
            if(w == "")
            {
                emptyIndex = i;
                continue;
            }
            b[w[0] - 'a'].push_back(i);
            e[w[w.size() -1 ] - 'a'].push_back(i);
        }
        if(emptyIndex != -1)
        {
            for(int i = 0;i< words.size();i++)
            {
                if(i!=emptyIndex && isPalindrome(words[i]))
                {
                    res.push_back(vector<int>{i,emptyIndex});
                    res.push_back(vector<int>{emptyIndex,i});
                }
            }
        }

        for(int i = 0;i<26;i++)
        {
            for(int x:b[i])
            {
                for(int y:e[i])
                {
                    if(x != y && isPalindrome(words[x] + words[y]))
                    {
                        //cout<<words[x]+words[y]<<endl;
                        res.push_back({x,y});
                    }
                }
            }
        }
        return res;
    }
};

/*官方哈希*/
class Solution {
public:
    bool isPalindrome(string str)
    {
        string temp = str;
        reverse(str.begin(),str.end());
        return temp == str;
    }
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> b(26),e(26);
        vector<vector<int>> res;
        int emptyIndex = -1;
        for(int i = 0;i< words.size();i++)
        {
            string& w = words[i];
            if(w == "")
            {
                emptyIndex = i;
                continue;
            }
            b[w[0] - 'a'].push_back(i);
            e[w[w.size() -1 ] - 'a'].push_back(i);
        }
        if(emptyIndex != -1)
        {
            for(int i = 0;i< words.size();i++)
            {
                if(i!=emptyIndex && isPalindrome(words[i]))
                {
                    res.push_back(vector<int>{i,emptyIndex});
                    res.push_back(vector<int>{emptyIndex,i});
                }
            }
        }

        for(int i = 0;i<26;i++)
        {
            for(int x:b[i])
            {
                for(int y:e[i])
                {
                    if(x != y && isPalindrome(words[x] + words[y]))
                    {
                        //cout<<words[x]+words[y]<<endl;
                        res.push_back({x,y});
                    }
                }
            }
        }
        return res;
    }
};
/*字典树*/
class Solution {
public:
    struct node {
        int ch[26];
        int flag;
        node() {
            flag = -1;
            memset(ch, 0, sizeof(ch));
        }
    };

    vector<node> tree;

    void insert(string& s, int id) {
        int len = s.length(), add = 0;
        for (int i = 0; i < len; i++) {
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                tree.emplace_back();
                tree[add].ch[x] = tree.size() - 1;
            }
            add = tree[add].ch[x];
        }
        tree[add].flag = id;
    }

    int findWord(string& s, int left, int right) {
        int add = 0;
        for (int i = right; i >= left; i--) {
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                return -1;
            }
            add = tree[add].ch[x];
        }
        return tree[add].flag;
    }

    bool isPalindrome(string& s, int left, int right) {
        int len = right - left + 1;
        for (int i = 0; i < len / 2; i++) {
            if (s[left + i] != s[right - i]) {
                return false;
            }
        }
        return true;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        tree.emplace_back(node());
        int n = words.size();
        for (int i = 0; i < n; i++) {
            insert(words[i], i);
        }
        vector<vector<int>> ret;
        for (int i = 0; i < n; i++) {
            int m = words[i].size();
            for (int j = 0; j <= m; j++) {
                if (isPalindrome(words[i], j, m - 1)) {
                    int left_id = findWord(words[i], 0, j - 1);
                    if (left_id != -1 && left_id != i) {
                        ret.push_back({i, left_id});
                    }
                }
                if (j && isPalindrome(words[i], 0, j - 1)) {
                    int right_id = findWord(words[i], j, m - 1);
                    if (right_id != -1 && right_id != i) {
                        ret.push_back({right_id, i});
                    }
                }
            }
        }
        return ret;
    }
};

int main()
{
    Solution s;
    system("pause");
};