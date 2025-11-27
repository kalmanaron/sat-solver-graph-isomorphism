# Graph Isomorphism Problem
The Graph Isomorphism Problem is the computational problem of determining whether two finite graphs are isomorphic.  
Two graph 
$$G_1 = (V_1, E_1)$$
and 
$$G_2 = (V_2, E_2)$$
are isomorphic if there exists a bijection
$$f: V_1 \to V_2$$
such that 
$$(u, v) \in E_1 \iff (f(u), f(v)) \in E_2$$


# CNF encoding procedure
## Adjency Matrix Representation
I chose to represent the graphs using an adjacency matrix, this way I can easily access the edges of the graphs in constant time. At the same time every vertex can by represented by a number from 1 to n, where n is the number of vertices in the graph.
## Variables
To encode the problem in CNF, I realized that I need to create variables that represent the mapping of vertices from one graph to another. That way in the end I can check if the edges are preserved under this mapping.  
I created variables of the form
$$x_{i,j}$$
where $i \in V_1$, $j \in V_2$ so that:
$$(x_{i,j} = True) \iff (f(i) = j)$$

## Creating clauses
I need to split the problem into smaller subproblems and create clauses for each of them.
### $f$ is a function
TODO
### $f$ is defined for $\forall i \in V_1$
TODO
### $f$ is injective
TODO
### $f$ is surjective
TODO
### Edges are preserved
TODO

# User documentation
## Dependecies
TODO
## Running the code
TODO

# Description of included testing instances
those 3 i made myself

# Instance experiments and results
try to time how long it takes to solve the instances with different sizes