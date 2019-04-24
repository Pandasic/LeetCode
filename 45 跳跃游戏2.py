#尝试贪心
#144ms 14.7MB
class Solution:
    def jump(self, nums: 'List[int]') -> int:
        step = 0
        length = len(nums)
        itor = 0
        while itor < len(nums) - 1:
            next_itor = 0
            max_val = -100000
            for i in range(1,nums[itor]+1):
                if itor + i < length-1:
                    if (nums[itor+i] - nums[itor]+i) >= max_val:
                        max_val = nums[itor+i] - nums[itor]+i
                        next_itor = itor + i
                else:
                    return step +1
            if (max_val > length - 1):
                return step +2 
            itor = next_itor
            step += 1
        return step

s = Solution()
print(s.jump([3,2,1]))