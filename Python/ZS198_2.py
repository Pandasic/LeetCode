"""
5465. 子树中标签相同的节点数 显示英文描述 
通过的用户数162
尝试过的用户数259
用户总通过次数162
用户总提交次数297
题目难度Medium
给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）

边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。

返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。

树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。

 

示例 1：



输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
输出：[2,1,1,1,1,1,1]
解释：节点 0 的标签为 'a' ，以 'a' 为根节点的子树中，节点 2 的标签也是 'a' ，因此答案为 2 。注意树中的每个节点都是这棵子树的一部分。
节点 1 的标签为 'b' ，节点 1 的子树包含节点 1、4 和 5，但是节点 4、5 的标签与节点 1 不同，故而答案为 1（即，该节点本身）。
示例 2：



输入：n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
输出：[4,2,1,1]
解释：节点 2 的子树中只有节点 2 ，所以答案为 1 。
节点 3 的子树中只有节点 3 ，所以答案为 1 。
节点 1 的子树中包含节点 1 和 2 ，标签都是 'b' ，因此答案为 2 。
节点 0 的子树中包含节点 0、1、2 和 3，标签都是 'b'，因此答案为 4 。
示例 3：



输入：n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
输出：[3,2,1,1,1]
示例 4：

输入：n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
输出：[1,2,1,1,2,1]
示例 5：

输入：n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
输出：[6,5,4,1,3,2,1]
 

提示：

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
labels.length == n
labels 仅由小写英文字母组成
"""
class Solution:
    def countSubTrees(self, n: int, edges,labels):
        
        class Node:
            def __init__(self,index,char):
                self.char = char
                self.index = index
                self.father = None
                self.childs = []
                self.values = {}
                
        nodes = [Node(i,labels[i]) for i in range(len(labels))]
        nodes[0].father = -1
        for e in edges:
            if nodes[e[1]].father is None:
                nodes[e[0]].childs.append(e[1])
                nodes[e[1]].father = e[0]
            else:
                nodes[e[1]].childs.append(e[0])
                nodes[e[0]].father = e[1]

        def _countSubTrees(index):
            node = nodes[index]
            if len(node.values) > 0:
                return node.values
            node.values[node.char] = 1
            for i in node.childs:
                for k,v in _countSubTrees(i).items():
                    if k in node.values:
                        node.values[k] += v
                    else:
                        node.values[k] = v
            return node.values
        
        _countSubTrees(0)
        res= [0 for i in range(len(labels))]
        for n in nodes:
            res[n.index] = n.values[n.char]
        return res


class Solution:
    def countSubTrees(self, n: int, edges,labels):
        nodes = [None for i in range(len(labels))]
        hashMap = [[] for i in range(len(labels))]
        for e in edges:
            hashMap[e[0]].append(e[1])
            hashMap[e[1]].append(e[0])

        def bfs(index,father):
            if(nodes[index] != None):
                return nodes[index]
            res = {labels[index]:1}
            for e in hashMap[index]:
                r = {}
                if e != father:
                    r = bfs(e,index)
                for k,v in r.items():
                    if k in res:
                        res[k] += v
                    else:
                        res[k] = v
            nodes[index] = res
            return res
        bfs(0,-1)
        rtn = [nodes[i][labels[i]] for i in range(len(labels))]
        return rtn

s = Solution()
##print(s.countSubTrees(25,[[4,0],[5,4],[12,5],[3,12],[18,3],[10,18],[8,5],[16,8],[14,16],[13,16],[9,13],[22,9],[2,5],[6,2],[1,6],[11,1],[15,11],[20,11],[7,20],[19,1],[17,19],[23,19],[24,2],[21,24]],"hcheiavadwjctaortvpsflssg"))
print(s.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))