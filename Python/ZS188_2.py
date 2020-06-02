class Solution:
    def countTriplets(self, arr) -> int:
        count = 0
        #print(arr)
        dp = []
        for i in range(len(arr)):
            for k in range(i+1,len(arr)):
                res = arr[i]
                for x in range(i+1,k+1):
                    res = res^arr[x]
                if res == 0:
                    dp.append((i,k))
                    count += k - i
        return count

s = Solution()
print(s.countTriplets([2,3,1,6,7]))
print(s.countTriplets([1,1,1,1,1]))
#print(s.countTriplets([2,3]))
print(s.countTriplets([1,3,5,7,9]))
print(s.countTriplets([7,11,12,9,5,2,7,17,22]))\
#print(s.countTriplets([2,2]))
