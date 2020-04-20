"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
通过次数40,694提交次数55,491

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class mySolution:
    def combine(self, n: int, k: int):
        res = set()
        def part(now,begin):
            """
            now:当前
            begin:选择范围得开始
            """
            if len(now) == k:
                res.add(tuple(now))
            
            if now == []:
                b = begin
            else:
                b = max(now)

            for i in range(b,n+1):
                if i not in now:
                    p = now[:]
                    p.append(i)
                    part(p,begin)

        for b in range(1,n+1):
            part([],b)
        return list(res)

#官方 回溯
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output


s = Solution()
print(s.combine(4,2))