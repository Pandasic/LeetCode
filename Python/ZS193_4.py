"""
5188. 树节点的第 K 个祖先 显示英文描述 
通过的用户数46
尝试过的用户数230
用户总通过次数47
用户总提交次数301
题目难度Hard
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

 

示例：



输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
 

提示：

1 <= k <= n <= 5*10^4
parent[0] == -1 表示编号为 0 的节点是根节点。
对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
0 <= node < n
至多查询 5*10^4 次
"""
class TreeAncestor:
    def __init__(self, n: int, parent):
        self.n = n
        self.parents = parent
        self.dp = [[n+1 for i in range(n)] for i in range(n)]

        self.dp[0] = parent

        for i in range(1,len(self.dp)):
            for j in range(n):
                if parent[j] > 0:
                    self.dp[i][j] = self.dp[i-1][parent[j]]
                else:
                    self.dp[i][j] = -1

        print(self.dp)

    def getKthAncestor(self, node: int, k: int) -> int:
        k = k-1
        if k<0:
            return node
        if k >= len(self.dp):
            return -1
        return self.dp[k][node]

s = TreeAncestor(10,[-1,0,0,1,2,0,1,3,6,1])

args = ([8,6],[9,7],[1,1],[2,5],[4,2],[7,3],[3,7],[9,6],[3,5],[8,8])
for a in args:
    print(s.getKthAncestor(a[0],a[1]))

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)