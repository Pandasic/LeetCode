# 大神用素数表 每个素数代表一个字母
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        nu = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        for s in strs:
            k = 1
            for c in s:
                k *= nu[ord(c)-ord('a')]
            if k not in res.keys():
                res[k] = [s]
            else:
                res[k] += [s]
        return list(res.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))