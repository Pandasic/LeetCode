import os
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        with open("data_37.txt",'w') as f:
            f.write("")
        self.solveSudoku_part(board,0,0)

    def solveSudoku_part(self, board,x,y) -> None:
        with open("data_37.txt",'a') as f:
            f.write(str(board))
            f.write("\n")
        if board[y][x] != ".":
            if x == 8 and y == 8:
                return True
            if x == 8:
                return self.solveSudoku_part(board,0,y+1)
            else:
                return self.solveSudoku_part(board,x+1,y)
        else:
            for i in range(1,10):
                board[y][x] = str(i)
                if self.isValid_Block(board,x,y):
                    if x == 8 and y == 8:
                        return True
                    if x == 8:
                        if (self.solveSudoku_part(board,0,y+1)):
                            return True
                    else:
                        if self.solveSudoku_part(board,x+1,y):
                            return True
            board[y][x]= "."
            return False

    def isValidSudoku(self, board: "list[list[str]]") -> bool:
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and not self.isValid_Block(board,i,j):
                    print(j,i)
                    return False
        return True

    def isValid_Block(self, board: "list[list[str]]",x,y) -> bool:
        #Row
        for i in range(9):
            if i != x and board[y][i] == board[y][x]:
                return False
        #Line
        for i in range(9):
            if i != y and board[i][x] == board[y][x]:
                return False
        
        #Block
        BX = x//3
        BY = y//3
        for i in range(3):
            for j in range(3):
                if not(BY*3+i == y  and BX*3+j == x) and board[BY*3+i][BX*3+j] == board[y][x]:
                    return False
        
        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
[['5', '3', '4', '6', '7', '8', '9', '1', '2'],
 ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
 ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
 ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
 ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
 ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
 ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
 ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
 ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
s = Solution()
s.solveSudoku(board)