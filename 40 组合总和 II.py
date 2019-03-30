class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(remain,path,level):           
            if not remain:
                if path not in res:
                    res.append(path)
                return

            newLevel = level
            for i in range(level,len(candidates)):
                if candidates[i]> remain:
                    break
                elif path and candidates[i]<path[-1]:
                    continue
                else:
                    dfs(remain-candidates[i],path+[candidates[i]],newLevel+1)
                newLevel += 1
        
        dfs(target,[],0)
        return res