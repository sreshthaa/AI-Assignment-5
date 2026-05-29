import math

board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]


def print_board():

    for row in board:

        print(row)

    print()


def winner(b):

    lines=[]

    lines.extend(b)

    lines.extend([
        [b[0][0],b[1][0],b[2][0]],
        [b[0][1],b[1][1],b[2][1]],
        [b[0][2],b[1][2],b[2][2]]
    ])

    lines.append([b[0][0],b[1][1],b[2][2]])

    lines.append([b[0][2],b[1][1],b[2][0]])

    for line in lines:

        if line==['X','X','X']:

            return 'X'

        if line==['O','O','O']:

            return 'O'

    return None


def full(b):

    for row in b:

        if ' ' in row:

            return False

    return True


def minimax(b,isMax):

    win=winner(b)

    if win=='X':

        return 1

    if win=='O':

        return -1

    if full(b):

        return 0

    if isMax:

        best=-math.inf

        for i in range(3):

            for j in range(3):

                if b[i][j]==' ':

                    b[i][j]='X'

                    score=minimax(b,False)

                    b[i][j]=' '

                    best=max(best,score)

        return best

    else:

        best=math.inf

        for i in range(3):

            for j in range(3):

                if b[i][j]==' ':

                    b[i][j]='O'

                    score=minimax(b,True)

                    b[i][j]=' '

                    best=min(best,score)

        return best


board[0][0]='X'

board[1][1]='O'

board[0][1]='X'

print_board()

print(

"Minimax Score:",

minimax(board,True)

)
