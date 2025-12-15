# Generation ID: Hutch_1763363240578_47ziaom5e (前半)

def mya1(board, color):
    """
    オセロで最も多くの石が取れる位置を返す関数
    """
    size = len(board)
    opponent = 3 - color
    max_count = -1
    best_move = None

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(size):
        for col in range(size):
            if board[row][col] != 0:
                continue

            flip_count = 0

            for dr, dc in directions:
                temp_count = 0
                r, c = row + dr, col + dc

                while 0 <= r < size and 0 <= c < size and board[r][c] == opponent:
                    temp_count += 1
                    r += dr
                    c += dc

                if 0 <= r < size and 0 <= c < size and board[r][c] == color and temp_count > 0:
                    flip_count += temp_count

            if flip_count > max_count:
                max_count = flip_count
                best_move = (col, row)

    return best_move

# Generation ID: Hutch_1763363240578_47ziaom5e (後半)
othello.play(mya1)
