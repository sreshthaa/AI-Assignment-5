import random

wins=0

simulations=1000

for i in range(simulations):

    result=random.choice([0,1])

    wins+=result

print(

"Win Rate:",

wins/simulations

)
