class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def has_dup(cells):
            count = Counter(cells)
            for number, freq in count.items():
                if number != "." and freq > 1:
                    return True
            return False

        # rows
        for r in range(9):
            if has_dup(board[r]):
                return False

        # columns
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            if has_dup(column):
                return False

        # boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                box = []
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        box.append(board[r][c])
                if has_dup(box):
                    return False

        return True