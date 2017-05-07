import numpy as np

class projectGraph(object):
    xlength = 0
    ylength = 0
    tlength = 0
    edges = []

    def __init__(self, x, y, t, e):
        self.xlength = x
        self.ylength = y
        self.tlength = t
        if not e:
            self.createEdges()
        else:
            self.edges = e
        
        
    def createEdges(self):
        for i in range(self.xlength*self.ylength*self.tlength):
            if (self.getTop(i) > 0):
                self.edges.append([i,self.getTop(i),0])
            if (self.getLeft(self.getTop(i)) > 0):
                self.edges.append([i,self.getLeft(self.getTop(i)),1])
            if (self.getRight(self.getTop(i)) > 0):
                self.edges.append([i,self.getRight(self.getTop(i)),1])
            if (self.getFront(self.getTop(i)) > 0):
                self.edges.append([i,self.getFront(self.getTop(i)),1])
            if (self.getBack(self.getTop(i)) > 0):
                self.edges.append([i,self.getBack(self.getTop(i)),1])
            


    def getLeft(self, curr):
        if (curr%self.xlength > 0):
            return curr-1
        else:
            return -1

    def getRight(self, curr):
        if (curr%self.xlength + 1 < self.xlength):
            return curr +1
        else:
            return -1
    def getBack(self, curr):
        if ((curr/self.xlength)%self.ylength > 0):
            return curr-self.xlength
        else:
            return -1

    def getFront(self, curr):
        if ((curr/self.xlength)%self.ylength + 1 < self.ylength):
            return curr + self.xlength
        else:
            return -1
        
    def getBottom(self, curr):
        if ((curr/(self.xlength*self.ylength))%self.tlength > 0):
            return curr-(self.xlength*self.ylength)
        else:
            return -1

    def getTop(self, curr):
        if ((curr/(self.xlength*self.ylength))%self.tlength + 1 < self.tlength):
            return curr + (self.xlength*self.ylength)
        else:
            return -1

    def printEdges(self):
        print self.edges

    def getEdges(self):
        return self.edges

    def size(self):
        return self.xlength*self.ylength*self.tlength
    #def getFront(curr)
    def addOccupiedPath(self, path):
        modEdges = self.edges[:]
        for i in range(len(path)):
            for j in range(len(self.edges)):
                if self.edges[j][0] == path[i]:
                    try:
                        modEdges.remove(self.edges[j])
                    except:
                        print "not in list"
              
                if self.edges[j][1] == path[i]:
                    try:
                        modEdges.remove(self.edges[j])
                    except:
                         print "not in list"

                if i < len(path) - 1:
                    if path[i+1] == self.getLeft(self.getTop(path[i])):
                        if (self.edges[j][0] == self.getLeft(path[i])) and (self.edges[j][1] == self.getTop(path[i])):
                            try:
                                modEdges.remove(self.edges[j])    
                            except:
                                 print "not in list"
                            
                    if path[i+1] == self.getFront(self.getTop(path[i])):
                        if (self.edges[j][0] == self.getFront(path[i])) and (self.edges[j][1] == self.getTop(path[i])):
                            try:
                                modEdges.remove(self.edges[j])
                            except:
                                 print "not in list"
                    if path[i+1] == self.getBack(self.getTop(path[i])):
                        if (self.edges[j][0] == self.getBack(path[i])) and (self.edges[j][1] == self.getTop(path[i])):
                            try:
                                modEdges.remove(self.edges[j])
                            except:
                                 print "not in list"
                    if path[i+1] == self.getRight(self.getTop(path[i])):
                        if (self.edges[j][0] == self.getRight(path[i])) and (self.edges[j][1] == self.getTop(path[i])):
                            try:
                                modEdges.remove(self.edges[j])
                            except:
                                 print "not in list"
        self.edges = modEdges
            

def aStar(start, goal, graph):
        
    edges = graph.getEdges()

    openList = []
    closedList = []
    V = np.ones(graph.size())*1000*graph.size()

    V[start] = 0

    openList.append(start)
    #print V
    #print openList

    while (closedList.count(goal) == 0):
        if not openList:
            print "No path to goal"
            return -1;
        openListCostToGo = []
        for i in range(len(openList)):
            openListCostToGo.append(V[openList[i]])
        #print openList
        minVal = min(openListCostToGo)
        minInd = openListCostToGo.index(minVal)
        expandVert = openList[minInd]

        #Find all neighboring vertices to expanded vertex
        neighbors = []
        for i in range(len(edges)):
            if edges[i][0] == expandVert:
                neighbors.append([edges[i][1], edges[i][2]])

        #Calculate the value for each neighbor, add to open list
        for i in range(len(neighbors)):
            if (V[neighbors[i][0]] > V[expandVert]+neighbors[i][1]):
                V[neighbors[i][0]] = V[expandVert]+neighbors[i][1]
                openList.append(neighbors[i][0])

        openList.remove(expandVert)
        closedList.append(expandVert)

    traceback = goal
    path = [traceback]
    while traceback != start:
        neighborCostToGo = []
        neighbors = []
        for i in range(len(edges)):
            if edges[i][1] == traceback:
                neighborCostToGo.append(V[edges[i][0]])
                neighbors.append(edges[i][0])
        minVal = min(neighborCostToGo)
        minInd = neighborCostToGo.index(minVal)
        traceback = neighbors[minInd]
        path.append(traceback)

    path.reverse()
    return path

