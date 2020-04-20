class Solution:
    def searchRange(self, nums: "List[int]", target: int) -> int:
        pos = self.searchRange_part(nums,0,len(nums)-1,target)
        if pos == -1:
            return [-1,-1]
        itor = pos
        while (itor >=0 and nums[itor] == target):
            itor -= 1
        left = itor+1
        itor = pos
        while (itor <len(nums) and nums[itor] == target):
            itor += 1
        right = itor-1
        
        return [left,right]
    def searchRange_part(self, nums: "List[int]",low:int,high:int,target: int) -> int:
        if (low > high):
            return -1
        mid = int((low + high)/2)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.searchRange_part(nums, mid + 1, high, target)
        else:
            return self.searchRange_part(nums, low, mid - 1, target)