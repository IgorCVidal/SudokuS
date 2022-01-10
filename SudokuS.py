import numpy


board2 = [
    [0,0,0,7,9,0,0,5,0],
    [3,5,2,0,0,7,0,4,0],
    [0,0,0,0,0,0,0,8,0],
    [0,1,0,0,7,0,0,0,4],
    [6,0,0,3,0,1,0,0,8],
    [9,0,0,0,8,0,0,1,0],
    [0,2,0,0,0,0,0,0,0],
    [0,4,0,5,0,0,8,9,1],
    [0,8,0,0,3,7,0,0,0],
]
board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def check(bo,y,x,num):
    #Check the row
    for i in range(0,9):
        if bo[y][i] == num:
            return False
    #Check the column
    for i in range(0,9):
        if bo[i][x] == num:
            return False
    #Nominate the box
    boxl = (x//3)*3
    boxh = (y//3)*3
    #Check the box
    for i in range(0,3):
        for j in range(0,3):
            if bo[boxh+i][boxl+j] == num:
                return False        
    return True

def solve(bo):
    for y in range(len(bo)):
        for x in range(len(bo)):
            if bo[y][x] == 0 :
                for num in range(1,10):
                    if check(bo,y,x,num):
                        bo[y][x] = num
                        solve(bo)
                        bo[y][x] = 0
                return        
    print(numpy.matrix(bo))



print(numpy.matrix(board1))
print("solução ")
solve(board1)
