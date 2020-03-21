# socially-anxious-boids

Our goal is to implement a boids-like simulation of flocking behaviour and use it to find a set of rules that encourage proper social distancing in public spaces. Ideally, this set of rules can then be distributed digitally and analogously to reach out to as many people as possible.


## Ladder to success

 - Implement and visualize the classic Boids model (Reynolds 1987).
 - Define a metric and measures for proper social distancing (rolling average density distribution, nearest-neighbour distance...).
 - Find a set of rules on a 2D grid that is simple and encourages proper behaviour.
 - Add obstacles to the grid.
 - Try the rules on the most common network topologies.


## The boids model

The [boids model](https://dl.acm.org/doi/10.1145/37402.37406) is an agent-based artificial life program introduced by Craig Reynolds in 1986. Based on a set of simple rules, a complex collective behaviour emerges from the interaction of the agents. Boids-like simulations are used e.g. in video game engines to create realistic-looking bird swarms etc.

A pdf version of the paper can be found [here](https://team.inria.fr/imagine/files/2014/10/flocks-hers-and-schools.pdf).
