class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0];
        sum = 0;
        for  num in nums:
            if (sum > 0):
                sum += num;
            else:
                sum = num;
            res = Math.max(res, sum);
        return res
