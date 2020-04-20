class Solution:
    def permuteUnique(self, nums):
        coll = self.permuteUnique_part(nums)
        res = []
        for c in coll:
            if c not in res:
                res.append(c)
        return res

    def permuteUnique_part(self, nums):
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            n = nums[:]
            n.remove(nums[i])
            for c in self.permuteUnique_part(n):
                res.append([nums[i]] + c)
        return res

s = Solution()
print(s.permuteUnique([1,1,2]))