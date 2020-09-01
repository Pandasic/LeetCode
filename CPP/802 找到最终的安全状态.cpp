#include "include.hpp"
using namespace std;
/*
802. 找到最终的安全状态
在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。

现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 更具体地说, 存在一个自然数 K,  无论选择从哪里开始行走, 我们走了不到 K 步后必能停止在一个终点。

哪些节点最终是安全的？ 结果返回一个有序的数组。

该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数.  图以以下的形式给出: graph[i] 是节点 j 的一个列表，满足 (i, j) 是图的一条有向边。

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
这里是上图的示意图。
*/

/*并查集思想 逐步将重点和可行的点加入结果集中*/
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<bool> isEnd(graph.size(),false);
        vector<int> res;
        bool isupadte = true;

        while(isupadte)
        {
            isupadte = false;
            for(int i = 0;i< graph.size();i++)
            {
                if(!isEnd[i])
                {
                    int outCount = graph[i].size();
                    for(int o:graph[i])
                    {
                        if(isEnd[o])
                            outCount--;
                    }
                    if(outCount == 0)
                    {
                        isEnd[i] = true;
                        isupadte = true;
                        res.push_back(i);
                    }
                }
            }
        }
        sort(res.begin(),res.end());
        return res;
    }
};

/*反向图*/
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) 
    {
        int N  = graph.size();
        vector<bool> safe(N,false);

        vector<set<int>> ograph;
        vector<set<int>> rgraph;
        for (int i = 0; i < N; ++i) {
            ograph.push_back(set<int>());
            rgraph.push_back(set<int>());
        }

        queue<int> queue;

        for (int i = 0; i < N; ++i) {
            if (graph[i].size() == 0)
                queue.push(i);
            for (int j: graph[i]) {
                ograph[i].insert(j);
                rgraph[j].insert(i);
            }
        }

        while (!queue.empty()) {
            int j = queue.front();
            queue.pop();
            safe[j] = true;
            for (int i: rgraph[j]) {
                ograph[i].erase(j);
                if (ograph[i].empty())
                    queue.push(i);
            }
        }

        vector<int> ans;
        for (int i = 0; i < N; ++i) if (safe[i])
            ans.push_back(i);

        return ans;
    }
};

int main()
{
    Solution s;
    system("pause");
};