import numpy as np
import motionplanning as mp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xdim = 4
ydim = 4
tdim = 6

size = xdim*ydim*tdim

print size

a = np.array([(1,1,0),(1,1,1),(1,2,1),(1,0,1),(0,1,1),(2,1,1)])

start = [8,9,10,11]
goal = [size-5,size-6,size-7,size-8]
print goal
path = []
graph = mp.projectGraph(xdim,ydim,tdim, [])

graph.createEdges()
#graph.printEdges()

for i in range(len(start)):
    path.append(mp.aStar(start[i], goal[i], graph))
    #print path[i]
    graph.addOccupiedPath(path[i])

for i in range(len(start)):
    print path[i]

#print pathR



    


#print graph.xlength
#print graph.getTop(0)
#print graph.getBottom(0)
#print graph.getTop(15)
#print graph.getBottom(15)
