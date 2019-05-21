class Solution:
    def removeDuplicates(self, S: str) -> str:
        isChange = True
        S = S + '\0'
        #循环去重
        while isChange:
            isChange = False
            i = 0
            #用while 防止字符串改变导致的越界
            while (i < len(S)-1):
                if (S[i] == S[i+1]):
                    S = S[:i]+S[i+2:]
                    isChange = True
                i+=1
        return S[:-1]

s = Solution()
print(s.removeDuplicates("abccaba"))