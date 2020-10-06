#UniformCostSearch.py
#by YesayaYova
#with Python3

"""
UNIFORM COST SEARCH ALGORITHM
"""

def uniformCost(graph, goal, first):
    current   = first
    queue     = [first]
    queueCost = [0]
    routeList = [[first]]
    explored  = []
    
    while len(queue) > 0 :
        #choose lowest element in queue
        current = findLowest(queue, queueCost)
        
        #if found the goal
        if current == goal:
            print("Found!")
            break
            
        explored.append(current)
        
        #checking to each current's neighbour
        for neighbour in graph[current]:
            if (neighbour[0] not in explored) or (neighbour[0] not in queue):
                queue.append(neighbour[0])
                queueCost.append(neighbour[1])
        

def findLowest(queue, queueCost):
    pick = queueCost[0]
    
    #check to each cost in queueCost
    for i in range(len(queueCost)):
        if pick > queueCost[i]:
            pick = queueCost[i]
    
    #get the index of lowest cost
    index = queueCost.index(pick)
    
    return queue[index]
