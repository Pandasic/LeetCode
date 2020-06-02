class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        yy = ['a','e','i','o','u']
        maxCount = 0
        for i in range(len(s)-k+1):
            ns = s[i:i+k]
            count = 0
            for j in range(k):
                if ns[j] in yy:
                    count += 1
            maxCount = max(maxCount,count)
        return maxCount


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        yy = ['a','e','i','o','u']
        vals = []
        maxCount = 0;
        for i in range(len(s)):
            if s[i] in yy:
                vals.append(i)

        for i in range(len(vals)):
            count = 1
            while i+count <len(vals) and vals[i+count] - vals[i] <= k:
                count += 1
            maxCount = max(maxCount,maxCount)
        return maxCount