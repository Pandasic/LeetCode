class Solution:
    def divisorGame(self, N: int) -> bool:
        win = False
        num = N
        while num > 1:
            d = self.getMaxDivisor(num)
            num = int(num - d)
            win = not win
        return win

    def getMaxDivisor(self,num):
        for i in range(2,num+1):
            if (num % i == 0):
                return num/i

s = Solution()
print(s.divisorGame(4))