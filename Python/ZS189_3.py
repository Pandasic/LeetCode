"""
5414. 收藏清单 显示英文描述 
通过的用户数142
尝试过的用户数174
用户总通过次数143
用户总提交次数192
题目难度Medium
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。

请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

 

示例 1：

输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
示例 2：

输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1] 
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
示例 3：

输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]
 

提示：

1 <= favoriteCompanies.length <= 100
1 <= favoriteCompanies[i].length <= 500
1 <= favoriteCompanies[i][j].length <= 20
favoriteCompanies[i] 中的所有字符串 各不相同 。
用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompanies[j] 仍然成立。
所有字符串仅包含小写英文字母。
"""

#这方法居然过了？ NB 感觉还能优化。。

class Solution:
    def peopleIndexes(self, favoriteCompanies):
        dp = [[None for i in range(len(favoriteCompanies))]for j in range(len(favoriteCompanies))]
        def isSubColl(i,j):
            if dp[i][j] != None:
                return dp[i][j]
            c1 = favoriteCompanies[i]
            c2 = favoriteCompanies[j]
            if(len(c1) >len(c2)):
                for w in c2:
                    if w not in c1:
                        return 0
                else:
                    return 1
            else:
                for w in c1:
                    if w not in c2:
                        return 0
                else:
                    return -1
        
        rtn = []

        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)): 
                if i != j:
                    isSub = isSubColl(i,j)
                    if dp[i][j] == None:
                        dp[i][j] = isSub
                        dp[j][i] = -isSub
                    if(isSub<0):
                        break
            else:
                rtn.append(i)
        return rtn

s = Solution()
print(s.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(s.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))