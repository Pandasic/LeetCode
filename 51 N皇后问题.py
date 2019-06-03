class NQueens:
    def __init__(self,n = 8):
        self.chess = []
        self.width = 0
        self.count = 0
        self.results = []
        self.solveNQueens(n)

    def solveNQueens(self, n):
        self.width = n
        self.chess =[ [0 for i in range(n)] for i in range(n)]
        self.queens()
        return self.results
    
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
            
s = NQueens(8)
print(s.results)