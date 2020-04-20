class Solution:
    def longestArithSeqLength(self, A: list) -> int:
        max_count = 0
        dp = []
        for i in range(len(A)-1):
            for j in range(i+1,len(A)-1):
                t = A[i]
                d = A[j]-A[i]
                count = 2
                t = A[j]
                print(A[i] ,end=" ")
                print(A[j] ,end=" ")
                while (t + d) in A[j+1:]:
                    count += 1
                    t = t + d
                    print(t ,end=" ")
                if count > max_count:
                    max_count = count
                print()
        return max_count

s = Solution()
print(s.longestArithSeqLength([24,13,1,100,0,94,3,0,3]))
