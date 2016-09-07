def nextCellToFill(puzzle, i, j):
    for i in range(i,4):
        for j in range(j,4):
            if puzzle[i][j] == 0:
                return i,j
    for i in range(0,4):
        for j in range(0,4):
            if puzzle[i][j] == 0:
                return i,j
    return -1,-1

def isValid(puzzle, i, j, k):
    rowOk = all([k != puzzle[i][x] for x in range(4)])
    if rowOk:
        columnOk = all([k != puzzle[x][j] for x in range(4)])
        if columnOk:
            boxTopX, boxTopY = 2 *(i/2), 2 *(j/2)
            for x in range(boxTopX, boxTopX+2):
                for y in range(boxTopY, boxTopY+2):
                    if puzzle[x][y] == k:
                        return False
            return True
    return False

def solve(puzzle, i=0, j=0):
    i,j = nextCellToFill(puzzle, i, j)
    if i == -1:
        return True
    for x in range(1,5):
        if isValid(puzzle,i,j,x):
            puzzle[i][j] = x
            if solve(puzzle, i, j):
                return True
            puzzle[i][j] = 0
    return False

sudoku = [[1,0,3,0],
          [0,0,0,0],
          [2,0,4,0],
          [0,0,0,0]]

solve(sudoku)

for i in range(len(sudoku)):
    print sudoku[i]
