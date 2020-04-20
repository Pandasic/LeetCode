"""
5297. 跳跃游戏 III 显示英文描述 
用户通过次数125
用户尝试次数177
通过次数136
提交次数234
题目难度Medium
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。

请你判断自己是否能够跳到对应元素值为 0 的 任意 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。

 

示例 1：

输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 
示例 2：

输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true 
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 0 -> 下标 4 -> 下标 1 -> 下标 3
示例 3：

输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。 
 

提示：

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
"""
# 递归居然过了 = =??? 没超时？？？
class Solution:
    def canReach(self, arr , start: int) -> bool:
        return self.canReach_part(arr,start,[])

    def canReach_part(self,arr,index,path):
        #print(path)
        if arr[index] == 0:
            return True

        if index in path:
            return False

        res = False
        if  0 <= index + arr[index] < len(arr):
            res = res or self.canReach_part(arr, index + arr[index] ,path[:] + [index])
        
        if  0 <= index - arr[index] < len(arr):
            res = res or self.canReach_part(arr, index - arr[index] ,path[:] + [index])
        return res

s  = Solution()
#print(s.canReach(arr = [4,2,3,0,3,1,2], start = 5))
#print(s.canReach(arr = [4,2,3,0,3,1,2], start = 0))
#print(s.canReach(arr = [3,0,2,1,2], start = 2))
print(s.canReach(arr = [0,1], start = 1))

