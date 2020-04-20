"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
通过次数128,142提交次数272,057
"""
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #两个 指针 从后向前
        itor1 = m - 1
        itor2 = n - 1
        nowpos = m + n - 1 
        while itor1 >= 0 and itor2 >= 0:
            if nums1[itor1] > nums2[itor2]:
                nums1[nowpos] = nums1[itor1]
                itor1 -= 1
            else:
                nums1[nowpos] = nums2[itor2]
                itor2 -= 1
            nowpos -= 1
        if itor2 > 0:
            for i in range(itor2):
                nums1[i] = nums2[i]

        print(nums1)

s = Solution()
#s.merge([1,2,3,0,0,0],3,[2,5,6],3)
s.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)