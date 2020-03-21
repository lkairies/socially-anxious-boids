#randomized directions
import numpy as np
import matplotlib.pyplot as plt


Lx=1500
Ly=1500

lidlx=np.random.rand(1)*Lx
lidly=np.random.rand(1)*Ly


def initialize(xagents,yagents,Lx,Ly):
    for i in range(len(xagents)):
        xagents[i]=Lx*np.random.rand(1)
        yagents[i]=Ly*np.random.rand(1)

#kommt noch
def update_velocity_verlet(xes,yes,dt,xvel,yvel,xforce,yforce):
    xes=xes+dt*xvel+dt*dt*xforce/2
    yes=yes+dt*yvel+dt*dt*yforce/2
    #Calculate new forces!!
    dummy=rule_LJP(xes,yes)

    xvel=xvel+0.5*dt*xforce
    yvel=yvel+0.5*dt*yforce

    xvel=xvel+dt*0.5*np.array(dummy)[0,]
    yvel=yvel+dt*0.5*np.array(dummy)[1,]

    #per bdries for now
    xes[np.where(xes>Lx)]=xes[np.where(xes>Lx)]%Lx
    yes[np.where(yes>Lx)]=yes[np.where(yes>Ly)]%Ly
    return(xes,yes,xvel,yvel,xforce,yforce)


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

def update():
    print("15")

def sichtkegel():
    dalpha=pi/3.0
    if(hassome(dalpha,force)):
        print("no")



def rule_repulsive(boids):
    for i in range(len(boids)):
        if(distance(boids[i])<2):
            force=array([force[1],force[2]])
            #COM=
            #sum of the partners=center of mass
            #dosomething with Force
def rule_LJP(xes,yes):
    forcex=np.zeros(len(xes))
    forcey=np.zeros(len(xes))
    Forci=np.zeros(len(xes))
    for i in range(len(xes)):
            r=np.sqrt(pow(yes[i]-lidly[0],2)+pow(xes[i]-lidlx[0],2))
            Forci[i]=pow(0.0/(r),12)-pow(1/(r),6)
            forcey[i]=Forci[i]*np.cos((yes[i]-lidly[0])/(xes[i]-lidlx[0]))
            forcex[i]=Forci[i]*np.sin((yes[i]-lidly[0])/(xes[i]-lidlx[0]))
    return (forcex,forcey)



def rule_iseeu():
    if(sichtkegel(force)):
        force=-force


#noofagents can come from the ui
noofagents=20
xes=np.zeros(noofagents)
yes=np.zeros(noofagents)

grid=np.zeros((int(Lx/0.1),int(Lx/0.1)))

initialize(xes,yes,Lx,Ly)

grid_setup(0.1,0.1,Lx,Ly,grid)

#2 levels of propagation speeds:
#AND PARTICLES NEED TO REST INBETWEEN
xspeed1=0.1
xspeed2=1.0

yspeed1=0.1
yspeed2=1.0

vPhi=np.zeros(noofagents)
vR  =np.zeros(noofagents)

xF=0.0*np.random.rand(noofagents)*1000
yF=0.0*np.random.rand(noofagents)*1000
xvel=0.0*np.random.rand(noofagents)
yvel=0.0*np.random.rand(noofagents)
#xvel,yvel,xforce,yforce
#iwanttowatch is a bool from the ui

dt=1.0
iwanttowatch=1
#while iwanttowatch:

dummy=np.zeros((2,noofagents))

plt.plot(lidlx,lidly,'go')
for i in range(10000):


    dummy=update_velocity_verlet(xes,yes,dt,xvel,yvel,xF,yF)

    #print(dummy)
    xes=np.array(dummy)[0,]
    yes=np.array(dummy)[1,]
    xvel=np.array(dummy)[2,]#+np.random.rand()
    yvel=np.array(dummy)[3,]#+np.random.rand()
    xF=np.array(dummy)[4,]
    yF=np.array(dummy)[5,]
    #lets drag the grid with us!
    #grid_setup(0.1,0.1,Lx,Ly,grid)
    if((i%1000)==0):
        plt.plot(lidlx,lidly,'go')
        plt.plot(xes,yes,'ro')
        plt.xlim(0,Lx)
        plt.ylim(0,Ly)
        plt.show()

#initial speed blabla
#with random direction
#for i in range(len)
#    dir=np.random.rand(1)*2*pi
#    xes[i]=xes[i]+dt*speed1
