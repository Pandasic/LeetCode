"""
5474. 好叶子节点对的数量 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。

 

示例 1：

 



输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
示例 2：



输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
示例 3：

输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好叶子节点对是 [2,5] 。
示例 4：

输入：root = [100], distance = 1
输出：0
示例 5：

输入：root = [1,1,1], distance = 2
输出：1
 

提示：

tree 的节点数在 [1, 2^10] 范围内。
每个节点的值都在 [1, 100] 之间。
1 <= distance <= 10
"""
import tools
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def _countPairs(root,depth):
            if root is None:
                return None
            if root.left is None and root.right is None:
                return {depth:1}
            left  = _countPairs(root.left, depth + 1)
            right = _countPairs(root.right,depth + 1)
            if left is None:
                return right
            if right is None:
                return left

            if depth == 0:
                depth = 0
            maxD = max(max(left.keys()),max(right.keys()))
            for dl in left.keys():
                for dr in right.keys():
                    if dl + dr - depth*2 <= distance:
                        self.res += left[dl]*right[dr]

            newDict = {}
            for i in range(depth,maxD+1):
                nv = 0
                if i in left.keys():
                    nv += left[i]
                if i in right.keys():
                    nv += right[i]
                if nv != 0:
                    newDict[i] = nv
            return newDict

        _countPairs(root,0)
        return self.res


s = Solution()
print(s.countPairs(tools.stringToTreeNode("[78,15,81,73,98,36,null,30,null,63,32]"),6))