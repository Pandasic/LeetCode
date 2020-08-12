"""
题目描述
"""
class Solution:
    def getLastMoment(self, n, left, right):
        for i in range(len(right)):
            right[i] = n - right[i]
        return max(right + left)

s = Solution()
print(s.getLastMoment(20,[4,7,15],[9,3,13,10]))