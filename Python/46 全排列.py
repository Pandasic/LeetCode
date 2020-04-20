class Solution:
    def permute(self, nums):
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for c in self.permute([v for v in nums if v != nums[i]]):
                res.append([nums[i]] + c)
        return res

s = Solution()
print(s.permute([]))