# AI Assignment

Task 1: Minimax, Alpha Beta, Heuristic Alpha Beta, Monte Carlo Tree Search
Task 2: AI Travel Planner
Task 3: Knowledge Graph Discussion
Task 4: Bayesian Networks

TASK 1 
A. Minimax Search
Idea:
Two players:
MAX player → maximize score
MIN player → minimize score

Minimax(s)= Utility(s), terminal       
Minimax(s)= max(Minimax(children)), MAX
Minimax(s)= min(Minimax(children)), MIN


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


TASK 2 
# AI Based Travel Planner

## 1. Introduction
Travel planning is a complex process involving destination selection, cost estimation, accommodation planning, food selection, and itinerary generation. Users often spend considerable time comparing destinations, estimating budgets, and creating schedules.The objective of this project is to design an AI Based Travel Planner that automatically generates personalized travel plans using reusable knowledge bases and intelligent recommendation mechanisms.The system collects user preferences and generates travel recommendations, food suggestions, estimated costs, and day-wise itineraries.

## 2. Problem Statement
Traditional travel planning suffers from several issues:
* Large number of destinations available
* Difficulty estimating travel expenses
* Lack of personalization
* Time consuming itinerary generation
* Difficulty matching user preferences
The proposed AI Travel Planner addresses these issues using knowledge-driven recommendations and rule-based inference.

## 3. Objectives
The objectives of this system are:
* Recommend suitable travel destinations
* Reuse existing travel knowledge bases
* Generate personalized itineraries
* Recommend food based on user preferences
* Estimate overall travel cost
* Automate travel decision making

## 4. System Architecture
User Input Module
↓
Preference Analysis Module
↓
Knowledge Base
↓
Recommendation Engine
↓
Cost Assessment Module
↓
Itinerary Generator
↓
Final Travel Plan

## 5. User Input Module
The user provides travel preferences.
Inputs collected include:
* Budget
* Travel duration
* Travel interests
* Food preferences
* Transportation preferences
* Number of travelers
Example:
Budget: 25000 INR
Interest: Beach Tourism
Food Preference: Vegetarian
Duration: 3 Days
These inputs become constraints for recommendation generation.

## 6. Knowledge Base Reuse
The system reuses existing knowledge instead of generating everything from scratch.

### A. Tourist Place Knowledge Base
Contains:
* Destination Name
* Destination Type
* Average Cost
* Recommended Duration
* Popular Attractions
Example:
Goa
Type: Beach
Average Budget: 25000
Recommended Days: 3

### B. Food Recommendation Knowledge Base
Stores:
* Cuisine Categories
* Restaurant Types
* Food Preferences
* Vegetarian / Non Vegetarian Options

Example:
Vegetarian Options:
* Dosa
* Paneer Curry
* Veg Meals

### C. Transportation Knowledge Base
Stores:
* Bus Cost
* Train Cost
* Flight Cost
* Estimated Travel Expense

### D. Accommodation Knowledge Base
Stores:
* Hotel Cost
* Average Daily Stay Cost
* Location Information
* Ratings

## 7. Artificial Intelligence Components
The system applies several AI concepts.

### A. Recommendation Engine
The recommendation engine filters destinations according to user constraints.
Example:
IF:
Interest = Beach
AND
Budget >= Destination Cost
THEN:
Recommend Destination
This behaves similarly to content-based recommendation systems.

### B. Knowledge Reuse
Instead of building information manually every time, the system reuses:
* Travel databases
* Food datasets
* Cost information
* Domain ontologies
* Tourism knowledge
Knowledge reuse reduces computation and improves scalability.

### C. Rule Based Inference
Inference rules are used to personalize outputs.

Examples:
IF User prefers Vegetarian
THEN Remove Non Vegetarian Recommendations
IF Budget is Low
THEN Filter Expensive Destinations
IF Duration is Small
THEN Recommend Nearby Attractions
These rules allow intelligent decision making.

## 8. Destination Recommendation Process
Collect User Preferences
↓
Load Knowledge Bases
↓
Filter Destinations
↓
Calculate Costs
↓
Generate Personalized Recommendations
↓
Create Itinerary
↓
Return Travel Plan

## 9. Cost Assessment Module
The planner estimates total travel expense.
Total Cost = Transportation Cost* Accommodation Cost* Food Cost* Activity Cost
Example:
Transportation: 5000
Hotel: 7500
Food: 3000
Activities: 4000
Total Cost: 19500
This module helps users remain within budget.

## 10. Personalized Itinerary Generation
After selecting a destination, the system generates day-wise plans.
Example:
Day 1:
* Arrival
* Beach Visit
* Lunch Recommendation
* Dinner Recommendation
Day 2:
* Sightseeing
* Local Attractions
* Food Suggestions
Day 3:
* Shopping
* Return Journey
This allows automated tour creation.

## 11. Python Implementation Overview
The implementation consists of:
* Tourist Place Database
* Food Database
* Transportation Database
* Recommendation Logic
* Cost Calculator
* Itinerary Generator
The recommendation algorithm filters destinations according to constraints and produces travel plans automatically.

## 12. Advantages
* Personalized Recommendations
* Reduced Planning Time
* Automated Cost Estimation
* Knowledge Reuse
* Scalable Architecture
* Improved User Experience

## 13. Limitations
* Limited Dataset Size
* Static Knowledge Base
* No Real Time Updates
* No Dynamic Pricing Support
* Recommendations depend on available data quality

## 14. Future Improvements
* Real Time Weather Integration
* Hotel APIs
* Flight APIs
* Knowledge Graph Integration
* Machine Learning Recommendations
* Large Language Model Based Planning
* Voice Enabled Planning

## 15. Conclusion
The AI Based Travel Planner demonstrates how intelligent recommendation systems can automate travel planning through knowledge reuse, inference mechanisms, and personalized decision making.The system combines recommendation techniques, rule-based reasoning, and cost assessment to generate customized travel itineraries while minimizing user effort.


TASK 3 
KNOWLEDGE GRAPHS 

A Knowledge Graph (KG) is: A graph-based representation of knowledge where:
Nodes = Entities
Edges = Relationships
Properties = Attributes

They are used for:
Semantic Search
Recommendation Systems
Reasoning
Information Retrieval
Question Answering System

Components of Knowledge Graph
Entities : Objects being represented.
Relationships : Connections among entities.
Attributes : Properties of entities.

Tools for Building Knowledge Graphs
1.Neo4j
Used for: Graph Database Storage, Querying using Cypher, Visualization

2.Protégé
Used for: Ontology Design, OWL Modelling, Semantic Web Applications

3.Apache Jena
Provides: RDF Processing, SPARQL Queries, Knowledge Representation

4. Python Libraries
NetworkX
Used for: Graph Creation, Graph Analysis, Visualization

TASK 4
BAYESIAN NETWORKS 
A Bayesian Network is a Directed Acyclic Graph (DAG).Nodes represent variables.Edges represent dependencies.Conditional Probability Tables represent probabilities

Bayesian Network Components
Nodes : Represent variables.
Edges : Represent dependencies.
Conditional Probability Table (CPT) : Stores conditional probabilities.

Tools for Bayesian Networks
pgmpy :
Provides:
Bayesian Modelling
Inference
Learning
Probabilistic Reasoning

GeNIe
used for:
GUI Based Modelling
Inference Visualization

BayesiaLab
Used for:
Large Bayesian Systems
Analytics

PyMC
Used for:
Probabilistic Programming
Bayesian Statistics

