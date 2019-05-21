from queue import Queue
class Solution:
    def lastStoneWeight(self, stones = []) -> int:
        stones.sort(reverse = True)
        while len(stones) > 1:
            v = stones[0] - stones[1]
            stones = stones[2:]
            #插入排序
            if (v > 0):
                for i in range(len(stones)):
                    if stones[i] < v:
                        stones.insert(i,v)
                        break
                else:
                    stones.append(v)
            print(stones)
        if (len(stones) > 0):
            return stones[0]
        else:
            return 0

s = Solution()
s.lastStoneWeight([2,7,4,1,8,1])
