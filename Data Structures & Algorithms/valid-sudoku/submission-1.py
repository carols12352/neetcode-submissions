class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            cnt = Counter(col)
            for item, idx in cnt.items():
                if item != '.' and idx > 1:
                    return False
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                sqa = []

                for i in range(3):
                    for j in range(3):
                        sqa.append(board[row+i][col+j])
                
            
                cnt = Counter(sqa)
                for item, idx in cnt.items():
                    if item != '.' and idx > 1:
                        return False


        for i in range(9):
            cnt = Counter(board[i])
            for item, idx in cnt.items():
                if item != '.' and idx > 1:
                    return False
        return True
