import random

#empty spaces are negative one
puzzle = [

            [3, -1,  9,   4, -1, 7,   5, -1,  8],
            [7, -1,  6,  -1, -1, 5,  -1, -1, -1],
            [4, -1,  2,   6, -1, 3,   1,  9, -1],

            [9,  7,  4,   1,  3,-1,  -1, -1, -1],
            [2, -1, -1,  -1, -1,-1,   7, -1, -1],
            [8,  3, -1,   7,  6,-1,  -1,  1,  9],

            [-1,-1, -1,  -1,  7,-1,  -1,  2,  6],
            [-1,-1,  7,  -1, -1,-1,  -1,  5, -1],
            [ 1,-1, -1,  -1, -1, 6,   4,  7,  3]

        ]

def printPuzzle(puzzle):
    for r in range(9):
        if r%3 == 0 and r>0:
            print("\n"+"-"*9+"|"+"-"*9+"|"+"-"*9)
        else:
            print()
        for c in range(9):
            if c%3 == 0 and c>0:
                print("|",end="")

            if puzzle[r][c] == -1:
                print("-",end="  ")
            else:
                print(puzzle[r][c], end="  ")
        


def solvePuzzle(puzzle):
    row, col = findEmpty(puzzle)
    

    if row == None:
        print("\n\n\nSolution: ")
        printPuzzle(puzzle)
        return True
    
    for guess in range(1,10):
        if guessValid(row, col, guess, puzzle):
            puzzle[row][col] = guess
            
            #recursion to call puzzle since its mutating
            if solvePuzzle(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False

     
def guessValid(row, col, guess, puzzle):
    #check if guess in row
    if guess in puzzle[row]:
        return False 
    
    #check if guess in col
    colnums = [puzzle[r][col] for r in range(9)]
    if guess in colnums:
        return False

    #check if guess in 3x3 
    rStart = 0
    cStart = 0

    if row in [3, 4, 5]:
        rStart = 3
    elif row in [6,7,8]:
        rStart = 6

    if col in [3, 4, 5]:
        cStart = 3
    elif col in [6,7,8]:
        cStart = 6

    for r in range(rStart, rStart+3):
        for c in range(cStart, cStart+3):
            if guess == puzzle[r][c]:
                return False

    return True

def findEmpty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    
    return None, None

print("Unsolved Puzzle: ")
printPuzzle(puzzle)
solvePuzzle(puzzle)