class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numCnt = {}
        for row in board:
            for num in row:
                if num != ".":
                    numCnt[num] = numCnt.get(num, 0) + 1
                    if numCnt[num] > 1:
                        return False
            numCnt = {}

        for col in range(0, 9):
            numCnt = {}
            for row in range(0, 9):
                num = board[row][col]
                if num != ".":
                    numCnt[num] = numCnt.get(num, 0) + 1
                    if numCnt[num] > 1:
                        return False

        for box_row in range(0, 3):
            for box_col in range(0, 3):
                numCnt = {}
                for i in range(0, 3):
                    for j in range(0, 3):
                        num = board[box_row * 3 + i][box_col * 3 + j]
                        if num != ".":
                            numCnt[num] = numCnt.get(num, 0) + 1
                            if numCnt[num] > 1:
                                return False

        return True