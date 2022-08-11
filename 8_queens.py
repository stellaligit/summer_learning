def f(n, board):
    ''' place n queens to board. 
    return True when there is a solution. False when no solution.
    '''

    # we have 0 queens to place, that means we have found a solution.
    if n == 0:
        for i in range(8):
            print(board[i])
        return True
    
    for i in range(8):
        # try to place queen at (8-n, i)
        # update board to newBoard
        newBoard = []
        for j in range(8):
            newBoard.append(board[j].copy())
        newBoard[8-n][i] = 1

        # check if there is conflict
        if conflict(newBoard):
            continue
        
        # if we can place the remaining queens to newBoard, we have a solution.
        # otherwise continue the loop to check for other solution.
        if f(n-1, newBoard):
            return True

    # can't place queen at any of the 8 positions:
    return False

def diagonal1(board, start_row, start_col):
    queenCount = 0
    for delta in range(8):
        if start_row + delta > 7 or start_col + delta > 7:
            break
        if board[start_row + delta][start_col + delta] == 1:
            queenCount += 1
            if queenCount > 1:
                return True
    return False

def diagonal2(board, start_row, start_col):
    queenCount = 0
    for delta in range(8):
        if start_row + delta > 7 or start_col - delta < 0:
            break
        if board[start_row + delta][start_col - delta] == 1:
            queenCount += 1
            if queenCount > 1:
                return True
    return False

def conflict(board):
    # check each col has no more than 1 queen
    for col in range(8):
        queenCount = 0
        for row in range(8):
            if board[row][col] == 1:
                queenCount += 1
                if queenCount > 1:
                    return True

    # check \ diagonal has no more than 1 queen
    start_row = 0
    start_col = 0
    while start_col < 8:
        if diagonal1(board, start_row, start_col):
            return True
        start_col += 1

    start_row = 1
    start_col = 0
    while start_row < 8:
        if diagonal1(board, start_row, start_col):
            return True
        start_row += 1

    # check / diagonal has no more than 1 queen
    start_row = 0
    start_col = 0
    while start_col < 8:
        if diagonal2(board, start_row, start_col):
            return True
        start_col += 1
    
    start_row = 1
    start_col = 7
    while start_row < 8:
        if diagonal2(board, start_row, start_col):
            return True
        start_row += 1

    return False

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
        ]

f(8, board)