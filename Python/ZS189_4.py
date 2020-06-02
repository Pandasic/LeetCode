"""
5415. 圆形靶内的最大飞镖数量 显示英文描述 
通过的用户数31
尝试过的用户数84
用户总通过次数33
用户总提交次数133
题目难度Hard
墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。

投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。

请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。

 

示例 1：



输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
示例 2：



输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
示例 3：

输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
输出：1
示例 4：

输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
输出：4
 

提示：

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
"""

class Solution:
    def numPoints(self, points, r):
        def isInClircle(cent,aim):
            return  r**2 - (aim[0] - cent[0])**2 -(aim[1] - cent[1])**2 > 0

        bound_x = [+10e4,-10e4]
        bound_y = [+10e4,-10e4]
        
        for p in points:
            bound_x[0] = min(bound_x[0],p[0])
            bound_x[1] = max(bound_x[1],p[0])
            bound_y[0] = min(bound_y[0],p[1])
            bound_y[1] = max(bound_y[1],p[1])
        
        bound_x[0] += r**(1/2)
        bound_x[1] -= r**(1/2)
        bound_y[0] += r**(1/2)
        bound_y[1] -= r**(1/2)

        if (bound_x[1] <= bound_x[0] and bound_y[1] <= bound_y[0]):
            return len(points)
        elif (bound_x[1] <= bound_x[0]):
            bound_y[0] -= r**(1/2)
            bound_y[1] += r**(1/2)
            maxCount = 0
            for i in range(int(bound_y[0] + r),int(bound_y[1] - r + 1),1):
                resCount = 0
                for p in points:
                    if  i - r <= p[1] <= i +r:
                        resCount += 1
                maxCount = max(maxCount,resCount)
            return maxCount

        elif (bound_y[1] <= bound_y[0]):
            bound_x[0] -= r**(1/2)
            bound_x[1] += r**(1/2)
            maxCount = 0
            for i in range(int(bound_x[0] + r),int(bound_x[1] - r + 1),1):
                resCount = 0
                for p in points:
                    if  i - r <= p[0] <= i +r:
                        resCount += 1
                maxCount = max(maxCount,resCount)
            return maxCount
        else:
            bound_x[0] -= r**(1/2)
            bound_x[1] += r**(1/2)
            bound_y[0] -= r**(1/2)
            bound_y[1] += r**(1/2)
            maxCount = 0
            for i in range(int(bound_x[0] + r),int(bound_x[1] - r) + 1,1):
                for j in range(int(bound_y[0] + r),int(bound_y[1] - r + 1),1):
                    resCount = 0
                    for p in points:
                        if  (i - r <= p[0] <= i + r ) and (j - r <= p[1] <= j + r ): 
                            resCount += 1
                    maxCount = max(maxCount,resCount)
            return maxCount
           

s = Solution()
#print(s.numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2))
print(s.numPoints(points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5))