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

The basic behavioural observation that underlies the boids model is given by Reynolds:

"For a bird to participate in a flock, it must have behaviors that allow it to coordinate its movements with those of its flockmates. These behaviors are not particularly unique; all creatures have them to some degree. Natural flocks seem to consist of two balanced, opposing behaviors: a desire to stay close to the flock and a desire to avoid collisions within the flock [34]. It is clear why an individual bird wants to avoid collisions with its flockmates."

However, it is most likely that, in a large flock, an agent is not neccessarily aware of all other agents, but only to its nearest neighbours:

" Natural flocks seem to operate in exactly the same fashion over a huge range of flock populations. It does not seem that an individual bird can be paying much attention to each and every one of its flockmates. But in a huge flock spread over vast distances, an individual bird must have a localized and filtered perception of the rest of the flock. A bird might be aware of three categories: itself, its two or three nearest neighbors, and the rest of the flock."

### Simulation

Reynolds describes his notion of geometric flight, which is not crucial for our project, since we are simulating on a two dimensional grid. He gives three rules that generate flocking behaviour:

 - "Collision Avoidance: avoid collisions with nearby flockmates"
 - "Velocity Matching: attempt to match velocity with nearby flockmates"
 - "Flock Centering: attempt to stay close to nearby flockmates"

The explicit implementation is not given. We aim at creating a parametric model of those rules as implied by Reynolds:

"The three behavioral urges associated with flocking (and others to be discussed below) each produce an isolated suggestion about which way to steer the boid. These are expressed as acceleration requests. Each behavior says: "if I were in charge, I would accelerate in that direction." The acceleration request is in terms of a 3D vector that, by system convention, is truncated to unit magnitude or less. Each behavior has several parameters that control its function; one is a "strength," a fractional value between zero and one that can further attenuate the acceleration request. It is up to the navigation module of the boid brain to collect all relevant acceleration requests and then determine a single behaviorally desired acceleration. It must combine, prioritize, and arbitrate between potentially conflicting urges. The pilot module takes the acceleration desired by the navigation module and passes it to the flight module, which attempts to fly in that direction."

It is indicated that in more complex situations, such as obstacle avoidance, acceleration should not be given by a simple weighted average of the behavioural urges (rules) but by a prioritization of the rules. Activation functions or weights as functions of e.g. mutual distance or distance to obstacles could also be considered. In Reynolds' paper the weights for attraction/repulsion to nearest neighbours are chosen as a function of the inverse squared distance.

For the application in CGI, a global direction vector can be used to guarantee an average motion in the defined direction by the whole flock.

## TODO

 - Obstacle avoidance
