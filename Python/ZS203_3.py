'''
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dp = [0 for i in range(max(arr) + 2)]
        
        mCount = 0
        res = -1
        for i in range(len(arr)):
            v = arr[i]
            if dp[v-1] != 0 and dp[v+1] != 0:
                if dp[v-1] == m:
                    mCount -= 1
                if dp[v+1] == m:
                    mCount -= 1
                    
                nV = dp[v+1] + dp[v-1] + 1
                for j in range(v - dp[v-1], v + dp[v+1] + 1):
                    dp[j] = nV
                if dp[v] == m:
                    mCount += 1
                    
            elif dp[v-1] != 0:
                if dp[v-1] == m:
                    mCount -= 1
                nV = dp[v+1] + dp[v-1] + 1
                for j in range(v - dp[v-1], v + 1):
                    dp[j] = nV
                if dp[v] == m:
                    mCount += 1
            elif dp[v+1] != 0:
                if dp[v+1] == m:
                    mCount -= 1
                nV = dp[v+1] + dp[v-1] + 1
                for j in range(v, v +dp[v+1] + 1):
                    dp[j] = nV
                if dp[v] == m:
                    mCount += 1
            else:
                dp[v] = 1
                if dp[v] == m:
                    mCount += 1
            #print(mCount,dp)
            if mCount != 0:
                res = i+1
        
        #print()
        return res
                
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dp = []
        
        mCount = 0
        res = -1
        for i in range(len(arr)):
            v = arr[i]
            left = None
            right = None
            
            for j in range(len(dp)):
                p = dp[j]
                if p[1] == v-1:
                    left = p[:]
                if p[0] == v+1:
                    right = p[:]
            
            newVal = [v,v]
            if left is not None:
                newVal[0] = left[0]
                if left[1] - left[0] + 1 == m:
                    mCount -= 1
                del left
            
            if right is not None:
                newVal[1] = right[1]
                if right[1] - right[0] + 1 == m:
                    mCount -= 1
                del right
                
            dp.append(newVal)
            if newVal[1] - newVal[0] + 1 == m:
                mCount += 1
                    
            if mCount > 0:
                res = i+1
        
        #print()
        return res
'''               
            

class Solution:
    def findLatestStep(self, arr, m) -> int:
        dp = [[1,len(arr)]]
        
        mCount = 0
        res = -1
        for i in range(len(arr)-1,-1,-1):
            v = arr[i]
            print(dp)
            for k in range(len(dp)):
                p = dp[k]
                if v == p[0]:
                    p[0] = p[0] + 1
                    if p[1] - p[0] + 1 == m:
                        print("L")
                        return i
                    if p[1] < p[0]:
                        del dp[k]
                        break
                if v == p[1]:
                    p[1] = p[1] - 1
                    if p[1] - p[0] + 1 == m:
                        print("R")
                        return i
                    if p[1] < p[0]:
                        del dp[k]
                        break
                    
                    
                if p[0] < v < p[1]:
                    nl = [p[0],v-1]
                    nr = [v+1,p[1]]
                    del dp[k]
                    if nl[1] - nl[0] + 1 == m:
                        return i
                    if nr[1] - nr[0] + 1 == m:
                        return i
                    dp.append(nl)
                    dp.append(nr)
        return -1

s =Solution()
s.findLatestStep([3,1,5,4,2],2)