"""
5087. 活字印刷

你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

示例 1：

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
示例 2：

输入："AAABBC"
输出：188
 

提示：

1 <= tiles.length <= 7
tiles 由大写英文字母组成
"""
# 结果是对的 但是超时了。。

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        max_len = len(tiles)
        res = [set() for i in range(max_len+1)]
        
        #字符统计
        all_hist = self.calHist(tiles)

        #可能穷举
        for i in range(max_len):
            res[1].add(tiles[i])
        
        for i in range(2,max_len + 1):
            for w1 in res[i//2]:
                for w2 in res[i-i//2]:
                    #有效性检查
                    word_hist = self.calHist(w1+w2)
                    for k in word_hist.keys():
                        if word_hist[k]>all_hist[k]:
                            break
                    else:
                        res[i].add(w1+w2)
                        res[i].add(w2+w1)
                        
        count = 0
        for s in res:
            for w in s:
                count += 1
        return count
    
    def calHist(self,s):
        hist = {}
        for i in range(len(s)):
            if s[i] in hist.keys():
                hist[s[i]] += 1
            else:
                hist[s[i]] = 1
        return hist
    '''
    def numTilePossibilities(self, tiles: str) -> int:
        max_len = len(tiles)
        hist = {}
        for i in range(max_len):
            if tiles[i] in hist.keys():
                hist[tiles[i]] += 1
            else:
                hist[tiles[i]] = 1
        print(hist)
    '''
s = Solution()

