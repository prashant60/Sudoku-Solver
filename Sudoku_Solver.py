board = [
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

def solve(bo):
    find=empty(bo)
    if not find:
        return True
    else:
        i,j= find
    for val in range(1,10):
        if check(bo,val,i,j):
            bo[i][j]=val
            if solve(bo):
                return True
            bo[i][j]=0

    return False


def check(bo,val,x,y):
    for i in range(9):
        if bo[x][i]==val and y!=i:
            return False
    for i in range(9):
        if bo[i][y]==val and x!=i:
            return False
    st=x//3
    ed=y//3
    
    for i in range(st*3,(st*3)+3):
        for j in range(ed*3,(ed*3)+3):
            if val == bo[i][j] and (i,j)!=(x,y):
                return False
    return True



def print_board1(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - -')
        for j in range(9):
            if j%3==0 and j!=0:
                print('|', end=" ")
            print(bo[i][j], end=" ")
        print()


def empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                return (i,j)
    return None


print_board1(board)
print()
solve(board)
print("******* Solved Board *********")
print_board1(board)
