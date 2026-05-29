# AI Assignment

Task 1: Minimax, Alpha Beta, Heuristic Alpha Beta, Monte Carlo Tree Search
Task 2: AI Travel Planner
Task 3: Knowledge Graph Discussion
Task 4: Bayesian Networks


A. Minimax Search
Idea:
Two players:
MAX player → maximize score
MIN player → minimize score


             {    Utility(s), terminal
 Minimax(s)= {    max(Minimax(children)), MAX
             {    min(Minimax(children)), MIN


Objective: Implement the Minimax algorithm for Tic Tac Toe to determine the optimal move for an intelligent agent.
Algorithm Description: Minimax recursively explores all possible game states and assumes that both players play optimally. The MAX player attempts to maximize score while MIN attempts to minimize score.
Input:
Current board configuration
Output:
Optimal move score / best move
Working:
1. Generate possible moves
2. Recursively evaluate future states
3. Assign utility values
4. Select best possible move
Complexity:
Time Complexity:
O(b^d)
where:
b = branching factor
d = search depth
Space Complexity:
O(d)
Observation:
The algorithm successfully selects winning moves and blocks opponent moves.





             

B. Alpha Beta Search
Improvement over minimax.
Uses:
alpha → best MAX can guarantee
beta → best MIN can guarantee
Pruning condition: beta <= alpha 
Objective: Implement Alpha Beta pruning to reduce the number of nodes explored compared to Minimax.
Working:
1. Maintain alpha value
2. Maintain beta value
3. Prune branches when: beta <= alpha
Advantages: Reduces computation while preserving optimality.
Observation:
Produces same move as Minimax while exploring fewer states.


C. Heuristic Alpha Beta
Problem:
Large games cannot search full tree.
Solution:
Use:
Depth limit: 
Evaluation function
Example heuristic for Tic Tac Toe
Objective: Improve search efficiency by limiting depth and using heuristic evaluation.
Heuristic Used:
+10 for two X in a line
-10 for two O in a line
Search Process:
Search until depth limit
↓
Apply heuristic evaluation
↓
Return estimated score
Observation: Produces near optimal decisions with lower computation cost.



D. Monte Carlo Tree Search
Four phases:
1.Selection
2.Expansion
3.Simulation
4.Backpropagation
UCB = (wins/visits) + c(root over(ln(parentvisits)/visits))
Phases:
1. Selection
2. Expansion
3. Simulation
4. Backpropagation
Working: Random simulations are performed repeatedly and outcomes are used to estimate move quality.
Observation: As number of simulations increases, move quality improves.


