class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        candidates.sort(reverse = True)
        self.combinationSum_part(candidates,target,[])
        return self.res

    def combinationSum_part(self, candidates: 'List[int]', target: int,temp:'List[int]') -> 'List[List[int]]':
        if len(candidates) <= 0:
            return 
        nowVal = candidates[0]
        for i in range(target//nowVal,-1,-1):
            if target - nowVal*i == 0:
                temp += ([nowVal]*i)
                self.res.append(temp)
            else:
                self.combinationSum_part(candidates[1:],target - i*nowVal,temp + [nowVal]*i)

s = Solution()
print(s.combinationSum(candidates = [2,3,5], target = 8))