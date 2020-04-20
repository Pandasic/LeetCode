class Solution:
    def firstMissingPositive(self, nums) -> int:
        if nums == []:
            return 1
        temp = [0 for i in range(len(nums)+1)]
        for n in nums:
            if  0 < n < len(temp):
                temp[n] = 1
        for n in  range(1,len(temp)):
            if  temp[n] == 0:
                return n 
        else:
            return len(temp)

s = Solution()
s.firstMissingPositive([1])