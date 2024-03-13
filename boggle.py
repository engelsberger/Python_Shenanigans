def find_word_util(board, used, row, col, word):
    if len(word) == 0: return True
    used[row][col] = True
    for sub_row in range(row - 1, row + 2):
        for sub_col in range(col - 1, col + 2):
            if sub_row >= 0 and sub_row < len(board) and sub_col >= 0 and sub_col < len(board[0]) and not used[sub_row][sub_col] and word[0] == board[sub_row][sub_col]:
                if find_word_util(board, used, sub_row, sub_col, word[1:]): return True
    used[row][col] = False
    return False

def find_word(board, word):
    used = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if word[0] == board[row][col] and find_word_util(board, used, row, col, word[1:]): return True
    return False

testBoard = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]
    
print("BAILER: " + str(find_word(testBoard, "BAILER")))
print("RSCAREIOYBAILNEA: " + str(find_word(testBoard, "RSCAREIOYBAILNEA")))