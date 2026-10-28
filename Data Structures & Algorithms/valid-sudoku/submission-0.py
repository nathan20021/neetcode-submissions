class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row scan
        group = [[0,1,2], [3,4,5], [6,7,8]]
        for rowIndexGroup in group:
            rows = [board[rowIndex] for rowIndex in rowIndexGroup]
            seenBox = [set(), set(), set()]
            for row in rows:
                seenRow = set()
                for colIndex, num in enumerate(row):
                    if num == ".":
                        continue
                    boxIndex = colIndex // 3
                    if num in seenBox[boxIndex]:
                        return False
                    seenBox[boxIndex].add(num)
                    
                    if num in seenRow:
                        return False
                    seenRow.add(num)
            
        # Col Scan
        for colIndex in range(9):
            seenCol = set()
            for rowIndex in range(9):
                num = board[rowIndex][colIndex]
                if num == ".":
                    continue
                if num in seenCol:
                    return False
                seenCol.add(num)
        return True

        