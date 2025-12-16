from sakura import othello
othello.play()


# 定義: オセロの石の色
EMPTY = 0
BLACK = 1
WHITE = 2
   
# ----------------------------------------------------
# 戦略的な位置価値を定義 (Algorithm Strategy の改善)
# ----------------------------------------------------
# 8x8 盤面におけるマスの評価点 (高いほど重要)
POSITION_WEIGHTS = [
    [100, -20, 10, 5, 5, 10, -20, 100],  # 角(100)は最も重要
    [-20, -50, -2, -2, -2, -2, -50, -20], # Cマス、Xマス(-50, -20)は避ける
    [10, -2, 5, 1, 1, 5, -2, 10],      # 辺の安定マス(10)
    [5, -2, 1, 1, 1, 1, -2, 5],
    [5, -2, 1, 1, 1, 1, -2, 5],
    [10, -2, 5, 1, 1, 5, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100]
]

def myai(board, color):
    """
    オセロで最も多くの石が取れる位置を返す関数
    - アルゴリズム戦略として位置価値による評価関数を導入
    """
    board_size = len(board)
    opponent = BLACK if color == WHITE else WHITE
    
    # 総合評価点
    max_score = -float('inf')
    best_move = None
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] != EMPTY:
                continue
            
            total_flip_count = 0
            
            for dr, dc in directions:
                current_flip_count = 0
                r, c = row + dr, col + dc
                
                # 相手の石が連続しているかチェック
                while 0 <= r < board_size and 0 <= c < board_size and board[r][c] == opponent:
                    current_flip_count += 1
                    r += dr
                    c += dc
                
                # 自分の石で挟んでいるか、かつ間に相手の石があるかチェック
                is_valid_sandwich = (
                    0 <= r < board_size and 
                    0 <= c < board_size and 
                    board[r][c] == color and 
                    current_flip_count > 0
                )
                
                if is_valid_sandwich:
                    total_flip_count += current_flip_count
            
            # 手が有効な場合のみ、評価点を計算
            if total_flip_count > 0:
                # ----------------------------------------------------
                # 評価関数 (Algorithm Strategy のコア改善)
                # ----------------------------------------------------
                # スコア = (石の取得数 * 100) + 位置の戦略的価値
                # 石の取得数を重視しつつ、戦略的な優位性 (角、辺) を加味する
                position_value = POSITION_WEIGHTS[row][col]
                current_score = (total_flip_count * 100) + position_value
                
                # スコアを基に最適な手を更新
                if current_score > max_score:
                    max_score = current_score
                    best_move = (col, row) # (col, row) の形式を維持
            # 手が無効な場合 (total_flip_count == 0) はスキップ
            
    return best_move

# Generation ID: Hutch_1763363240578_47ziaom5e (後半)
othello.play(myai)
