def mya1(board, color):
    """
    改善版：ひっくり返し数＋位置評価で最良手を返すオセロAI
    """
    size = len(board)
    opponent = 3 - color

    pos_weight = [
        [1000, -500, 10, 10, 10, 10, -500, 1000],
        [-500, -200,  1,  1,  1,  1, -200, -500],
        [  10,    1,  5,  5,  5,  5,    1,   10],
        [  10,    1,  5,  1,  1,  5,    1,   10],
        [  10,    1,  5,  1,  1,  5,    1,   10],
        [  10,    1,  5,  5,  5,  5,    1,   10],
        [-500, -200,  1,  1,  1,  1, -200, -500],
        [1000, -500, 10, 10, 10, 10, -500, 1000]
    ]

      directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

     best_score = -10**9
     best_move = None

    for row in range(size):
        for col in range(size):
            if board[row][col] != 0:
                continue

            total_flip = 0

            for dr, dc in directions:
                r, c = row + dr, col + dc
                temp = 0
                while 0 <= r < size and 0 <= c < size and board[r][c] == opponent:
                    temp += 1
                    r += dr
                    c += dc

                 if 0 <= r < size and 0 <= c < size and board[r][c] == color and temp > 0:
                    total_flip += temp

                      if total_flip == 0:
                      　continue  # 非合法手

                       score = total_flip * 5 + pos_weight[row][col]

                         if score > best_score:
                          best_score = score
                           best_move = (row, col)
  return best_move
