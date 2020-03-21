import numpy as np

GRID_SIZE = 1000
MAX_VEL = 5
MAX_ACC = 2.5

class Boid():

    def __init__(self):
        rnd = np.random.uniform(low=-GRID_SIZE, high=GRID_SIZE, size=2)
        self.pos = np.array(rnd)

        rnd = np.random.uniform(low=-MAX_VEL, high=MAX_VEL, size=2)
        self.vel = np.array(rnd)

        rnd = np.random.uniform(low=-MAX_ACC, high=MAX_ACC, size=2)
        self.acc = np.array(rnd)


    def __str__(self):
        return str(self.pos)

    def update(self):
        self.pos += self.vel
        self.pos = self.pos%GRID_SIZE

        vel = self.vel + self.acc
        if np.linalg.norm(vel)<=MAX_VEL:
            self.vel=vel

        self.update_acceleration()


    def update_acceleration(self):
        self.acc += np.random.normal(size=2)


if __name__=='__main__':
    swarm = np.array([Boid() for _ in range(50)])
    for time in range(100):
        for i in range(50):
            swarm[i].update()
            print(swarm[i])


# TODO 
# - update_acceleration
# - random seed
# - update functions: acceleration must be updated first such that the current state of the flock is used and not a partial one!
