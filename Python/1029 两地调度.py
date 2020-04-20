class Solution:
    def twoCitySchedCost(self, costs) -> int:
        r = [(k, abs(p[0]-p[1]),p[0]>p[1]) for k,p in enumerate(costs)]
        r.sort(key = lambda x: -x[1])
        count = 0
        length = len(costs)
        res = 0
        for i in range(len(r)):
            n = r[i]
            if count >= length//2:
                res += costs[r[i][0]][0] 
                continue
            if i - count >= length//2:
                res += costs[r[i][0]][1] 
                continue
            if r[2]:
                count +=1
                res += costs[i][1]
            else:
                res += costs[i][0]
        return res



s = Solution()
print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
        