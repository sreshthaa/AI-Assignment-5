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

    # rows
    lines.extend(b)

    # columns
    for i in range(3):

        lines.append(
            [b[0][i],b[1][i],b[2][i]]
        )

    # diagonals

    lines.append(
        [b[0][0],b[1][1],b[2][2]]
    )

    lines.append(
        [b[0][2],b[1][1],b[2][0]]
    )

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


# Heuristic Evaluation Function

def heuristic(b):

    score = 0

    lines=[]

    lines.extend(b)

    for i in range(3):

        lines.append(
            [b[0][i],b[1][i],b[2][i]]
        )

    lines.append(
        [b[0][0],b[1][1],b[2][2]]
    )

    lines.append(
        [b[0][2],b[1][1],b[2][0]]
    )

    for line in lines:

        x=line.count('X')

        o=line.count('O')

        if x==2 and o==0:

            score += 10

        elif x==1 and o==0:

            score += 1

        elif o==2 and x==0:

            score -= 10

        elif o==1 and x==0:

            score -= 1

    return score


def alphabeta(
        b,
        depth,
        alpha,
        beta,
        isMax):

    win=winner(b)

    if win=='X':

        return 100

    if win=='O':

        return -100

    if full(b):

        return 0

    # Depth cutoff -> heuristic search

    if depth==0:

        return heuristic(b)

    if isMax:

        best=-math.inf

        for i in range(3):

            for j in range(3):

                if b[i][j]==' ':

                    b[i][j]='X'

                    value=alphabeta(
                        b,
                        depth-1,
                        alpha,
                        beta,
                        False
                    )

                    b[i][j]=' '

                    best=max(
                        best,
                        value
                    )

                    alpha=max(
                        alpha,
                        best
                    )

                    if beta<=alpha:

                        break

        return best

    else:

        best=math.inf

        for i in range(3):

            for j in range(3):

                if b[i][j]==' ':

                    b[i][j]='O'

                    value=alphabeta(
                        b,
                        depth-1,
                        alpha,
                        beta,
                        True
                    )

                    b[i][j]=' '

                    best=min(
                        best,
                        value
                    )

                    beta=min(
                        beta,
                        best
                    )

                    if beta<=alpha:

                        break

        return best


def best_move():

    best=-math.inf

    move=None

    for i in range(3):

        for j in range(3):

            if board[i][j]==' ':

                board[i][j]='X'

                score=alphabeta(
                    board,
                    4,              # depth limit
                    -math.inf,
                    math.inf,
                    False
                )

                board[i][j]=' '

                if score>best:

                    best=score

                    move=(i,j)

    return move


# TEST CASE

board[0][0]='X'
board[0][1]='X'

board[1][1]='O'

print("Current Board:")

print_board()

move=best_move()

print("Best Move:",move)
