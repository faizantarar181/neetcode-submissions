class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[] for _ in range(len(board))]

        for column in board:
            count_c = Counter(column)
            for number, freq in count_c.items():
                if number != ".":
                    if freq > 1:
                        return False
            row = 0
            for number in column:
                rows[row].append(number)
                row += 1

        for i in rows:
            count_r = Counter(i)
            for number, freq in count_r.items():
                if number != ".":
                    if freq > 1:
                        return False

        start = 0

        while start < 9:
            col_start = 0
            while col_start < 9:
                box = []
                for i in range(start, start + 3):
                    for j in range(col_start, col_start + 3):
                        box.append(board[i][j])
                count_b = Counter(box)
                for number, freq in count_b.items():
                    if number != ".":
                        if freq > 1:
                            return False
                col_start += 3
            start += 3

        return True