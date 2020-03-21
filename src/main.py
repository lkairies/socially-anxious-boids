#randomized directions
import numpy as np

def initialize(xagents,yagents,Lx,Ly):
    for i in range(len(xagents)):
        xagents[i]=Lx*np.random.rand(1)
        yagents[i]=Ly*np.random.rand(1)

#kommt noch
def update_velocity_verlet():
#    for i in range():
    print("nene")

#grid erstellen
def grid_setup(dx,dy,Lx,Ly,grid):
    grid=np.zeros((int(Lx/dx),int(Ly/dy)))
    for i in range(int(Lx/dx)):
        for j in range(int(Ly/dy)):
            grid[i,j]=i+j

#ggf statistik über dem grid erstellen
def densiting(agents):
    for i in range(len(agents)):
    #    if agents.x[i]>
        print("deine butter")

Lx=500
Ly=500
noofagents=200
xes=np.zeros(noofagents)
yes=np.zeros(noofagents)

grid=np.zeros((int(Lx/0.1),int(Lx/0.1)))

initialize(xes,yes,Lx,Ly)

grid_setup(0.1,0.1,Lx,Lx,grid)

for i in range(int(Lx/0.1)):
    print(grid[i,i])

for i in range(noofagents):
    print(xes[i])
    print(yes[i])

#iwanttowatch is a bool from the ui
#while iwanttowatch:
#    update()


#print(xes)
#print(yes)

#def function():
#

'''

     pos=zeros(len);
     vel=zeros(len); // 2m/s along x-axis
     acc=zeros(len); // no acceleration at first

    mass = 1.0;
    drag = 0.1;


        Vec3d new_pos = pos + vel*dt + acc*(dt*dt*0.5);
        Vec3d new_acc = apply_forces(); // only needed if acceleration is not constant
        Vec3d new_vel = vel + (acc+new_acc)*(dt*0.5);

        pos = new_pos;
        vel = new_vel;
        acc = new_acc;




    Vec3d apply_forces() const

    {

         grav_acc = Vec3d{0.0, 0.0}# -9.81 }; // 9.81m/s^2 down in the Z-axis
         drag_force = 0.5 * drag * (vel * abs(vel)); // D = 0.5 * (rho * C * Area * vel^2)
         drag_acc = drag_force / mass; // a = F/m

        return grav_acc - drag_acc;

    }

};

'''

#2 levels of propagation speeds:
speed1=0.1
speed2=1.0

#initial speed blabla
#with random direction
#for i in range(len)
#    dir=np.random.rand(1)*2*pi
#    xes[i]=xes[i]+dt*speed1
