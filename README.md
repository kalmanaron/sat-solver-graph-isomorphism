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
"Official" definition:  
$$\forall v \in V_1 : \exists! f(v) \in V_2$$

in the language of our variables:  
"There isn't any pair from $V_1$ that share the same image in $V_2$"  
$$(\forall i \in V_1 )(\forall m,n \in V_2, m \neq n)(\neg x_{i,m} \lor \neg x_{i,n})$$


### $f$ is defined for $\forall i \in V_1$
"Official" definition:
$$\forall v \in V_1 : \exists f(v) \in V_2$$

in the language of our variables:  
"For every vertex in $V_1$ there is at least one vertex in $V_2$ that is its image"
$$(\forall i \in V_1)(x_{i,0} \lor x_{i,1} \lor ... \lor x_{i,|V_2|-1})$$


### $f$ is injective
"Official" definition:
$$\forall u,v \in V_1, u \neq v : f(u) \neq f(v)$$

in the language of our variables:  
"There isn't any pair from $V_2$ that share the same preimage in $V_1$"
$$(\forall j \in V_2)(\forall m,n \in V_1, m \neq n)(\neg x_{m,j} \lor \neg x_{n,j})$$


### $f$ is surjective
"Official" definition:
$$\forall w \in V_2 : \exists v \in V_1 : f(v) = w$$

in the language of our variables:  
"For every vertex in $V_2$ there is at least one vertex in $V_1$ that maps to it"
$$(\forall j \in V_2)(x_{0,j} \lor x_{1,j} \lor ... \lor x_{|V_1|-1,j})$$


### Edges are preserved
"Official" definition:
$$\forall u,v \in V_1 : (u,v) \in E_1 \iff (f(u), f(v)) \in E_2$$
in the language of our variables:  
"There doesn't exist any edge in $E_1$ that is not mapped to an edge in $E_2$ and vice versa"  
  
$(\forall u,v \in V_1)(\forall i,j \in V_2):$  
$(((u,v) \in E_1 \space \& \space (i,j) \not\in E_2) \lor ((u,v) \not\in E_1 \space \& \space (i,j) \in E_2) \implies (\neg x_{u,i} \lor x_{v,i}))$

# User documentation
## Dependecies
### Glucose SAT solver
The program requires the Glucose SAT solver to be installed and compiled in a directory namde "glucose" next to the main program directory. It relies on the version 4.2.1 accessible at: 
https://github.com/audemard/glucose/
### Python 3.12
The program requires Python 3.12 or higher to run.
## Running the code
### Command line usage
To run the program, naviage the the folder called "sat-solver-graph-isomorphism" and run the following command:
```
python .\program.py <path_to_graph1> <path_to_graph2> <options>
```

# Description of included testing instances
those 3 i made myself

# Instance experiments and results
try to time how long it takes to solve the instances with different sizes