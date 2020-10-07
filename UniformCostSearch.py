#UniformCostSearch.py
#by YesayaYova
#with Python3

"""
UNIFORM COST SEARCH ALGORITHM
"""

def uniformCost(graph, goal, first):
    current      = first
    currentCost  = 0
    currentRoute = [first]
    
    queue      = [first]
    queueCost  = [0]
    
    routeList  = [[first]]
    explored   = []
    
    while len(queue) > 0 :
        
        #if found the goal
        if current == goal:
            print("Found!")
            break
            
        explored.append(current)
        
        #checking to each current's neighbour
        for neighbour in graph[current]:
            if (neighbour[0] not in explored) or (neighbour[0] not in queue):
                queue.append(neighbour[0])
                queueCost.append(neighbour[1]+currentCost)
        
        for neighbour in graph[current]:
            if (neighbour[0] not in explored):
                x = []
                for i in range(len(currentRoute)):
                        x.append(currentRoute[i])
                    x.append(neighbour[0])
                    routeList.append(x)
        
        #choose lowest element in queue
        lowest, idLowest  = findLowest(queue, queueCost, routeList)
        
        current = queue.index()
        
        
def findLowest(queue, queueCost, routeList):
    pick = queueCost[0]
    x = 0
    
    #check to each cost in queueCost
    for i in range(len(queueCost)):
        if pick > queueCost[i]:
            pick = queueCost[i]
            x = i
    
    #get the index of lowest cost
    
    return pick, x
