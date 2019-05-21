class Solution:
    def __init__(self):
        self.chess = []
        self.width = 0
        self.count = 0
    def solveNQueens(self, n):
        self.width = n
        self.chess =[ [0 for i in range(n)] for i in range(n)]
        self.queens()
        print(self.count)
    
    def queens(self,y = 0,queens = []):
        for x in range(self.width):
            if self.check(x,y,queens):#位置不冲突
                print("%d,%d 成功"%(x,y))
                if y == self.width-1:
                    print(queens)
                    self.count += 1
                self.queens(y + 1,queens[:] + [(x,y)])
    
    def check(self,x,y,queens):
        for px,py in queens:
            if x==px or y ==py or abs(x-px) == abs(y-py):
                return False 
        return True
            
s = Solution()
s.solveNQueens(8)