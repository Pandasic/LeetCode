class Solution:
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

board = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
 ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
 ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
 ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
 ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
 ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
 ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
 ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
 ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
s = Solution()
print(s.isValidSudoku(board))