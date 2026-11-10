class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squs = [set() for _ in range(9)]
        for i in range(9):
            rl = len(rows[i])
            for j in range(9):
                cl = len(cols[j])
                squi = squs[int(i/3) * 3 + int(j/ 3)]
                sl = len(squi)
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squi.add(board[i][j])
                    print(i,j)
                    print("rows: ", rows)
                    print("cols: ", cols)
                    print("squs: ", squs)
                    if len(rows[i]) == rl or len(cols[j]) == cl or len(squi) == sl:
                        return False
                    else:
                        rl = len(rows[i])
                        cl = len(cols[j])
                        sl = len(squi)
        return True
                    
                    

