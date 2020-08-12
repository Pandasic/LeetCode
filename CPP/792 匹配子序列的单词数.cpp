#include "include.hpp"
using namespace std;
/*
792. 匹配子序列的单词数
给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。

示例:
输入: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出: 3
解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
注意:

所有在words和 S 里的单词都只由小写字母组成。
S 的长度在 [1, 50000]。
words 的长度在 [1, 5000]。
words[i]的长度在[1, 50]。
通过次数4,649提交次数11,024
*/

class Solution {
public:
    int numMatchingSubseq(string t, vector<string>& words) {
        int res = 0;
        for(string& s:words)
        {
            if(s.size() == 0)
            {
                ++res;
                break;
            }
            int itors = 0,itort = 0;
            while (s[itors] != '\0' && t[itort] != '\0')
            {
                if(s[itors] == t[itort])
                {
                    ++itors;
                }
                ++itort;
            }
            if (s[itors] == '\0')
                ++res;
        }
        return res;
    }
};

class Solution {
public:
    int numMatchingSubseq(string t, vector<string>& words) {
        vector<list<queue<char>>> temp(26,list<queue<char>>());
        for(auto s:words)
        {
            queue<char> q;
            for(auto c:s)
            {
                q.push(c);
            }
            temp[q.front() - 'a'].push_back(q);
        }
        int res = 0;
        for(auto c:t)
        {
            list<queue<char>> li = temp[c - 'a'];
            int len = li.size();
            for(int i = 0; i<len; i++)
            {
                queue<char> q = li.front();
                li.pop_front();
                q.pop();
                if(q.size() == 0)
                    ++res;
                else
                    temp[q.front() - 'a'].push_back(q);
            }
        }
        return res;
    }
};

class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        vector<queue<pair<int, int>>> buckets(26);
        for(int i = 0; i < words.size(); i++){
            buckets[words[i][0]-'a'].push({i, 0});
        }
        int res = 0;
        for(auto c: S){
            queue<pair<int, int>> & q = buckets[c-'a'];
            for(int i = q.size(); i > 0; i--){
                auto [wordIndex, posIndex] = q.front();
                q.pop();
                posIndex++;
                if(posIndex == words[wordIndex].length()){
                    res++;
                }
                else{
                    buckets[words[wordIndex][posIndex] - 'a'].push({wordIndex, posIndex});
                }
            }
        }
        return res;
    }
};

int main()
{
    Solution s;
    system("pause");
};