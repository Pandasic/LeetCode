class Solution:
    def __init__(self):
        self.chess = []
        self.width = 0
        self.count = 0
        self.results = []

    def solveNQueens(self, n):
        self.width = n
        self.chess =[ [0 for i in range(n)] for i in range(n)]
        self.queens()
        return self.res2QusRes()
    
    def res2QusRes(self):
        all_res = []
        for q in self.results:
            sgl_res = ["."*self.width]*self.width
            for  p in q:
                sgl_res[p[0]] = sgl_res[p[0]][:p[1]]+'Q'+sgl_res[p[0]][p[1]+1:]
            all_res.append(sgl_res)
        return all_res

    def queens(self,y = 0,queens = []):
        for x in range(self.width):
            if self.check(x,y,queens):#位置不冲突
                if y == self.width-1:
                    self.results += [queens+[(x,y)]]
                    self.count += 1
                self.queens(y + 1,queens[:] + [(x,y)])
    
    def check(self,x,y,queens):
        for px,py in queens:
            if x==px or y ==py or abs(x-px) == abs(y-py):
                return False 
        return True

s = Solution()
s.solveNQueens(4)