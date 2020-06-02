class Solution:
    def buildArray(self, target, n):
        n = max(target)
        res = []
        for i in range(1,n+1):
            res.append("Push")
            if i not in target:
                res.append("Pop")
        return res

s = Solution()
print(s.buildArray([],0))