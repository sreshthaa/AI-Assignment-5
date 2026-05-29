import math

def alphabeta(depth,maxPlayer,alpha,beta):

    if depth==0:

        return 3

    if maxPlayer:

        value=-math.inf

        for i in range(2):

            value=max(
                value,
                alphabeta(
                    depth-1,
                    False,
                    alpha,
                    beta
                )
            )

            alpha=max(alpha,value)

            if beta<=alpha:

                break

        return value

    else:

        value=math.inf

        for i in range(2):

            value=min(
                value,
                alphabeta(
                    depth-1,
                    True,
                    alpha,
                    beta
                )
            )

            beta=min(beta,value)

            if beta<=alpha:

                break

        return value


print(

alphabeta(

4,

True,

-math.inf,

math.inf

)

)
