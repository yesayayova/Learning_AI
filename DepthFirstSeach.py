#DepthFirstSearch.py
#by YesayaYova
#with Python3

"""
    DEPTH FIRST SEARCH ALGORITHM
    with input is a graph
"""

def DFS(graph, goal, first):
    explored = [first]
    queue    = []
    current  = first
    
    while True:        
        #if goal was found
        if current == goal:
            print ("\nFound!")
            backtrack = True
            break
        
        #check on each current's neighbour 
        for neighbour in graph[current]:
            if neighbour not in explored: 
                queue.append(neighbour)
        
        print(current, end=" ")
        explored.append(current)
        current = queue.pop()
        
        #if goal wasn't found
        if len(queue) == 0:
            print(". . .\nNot Found!")
            backtrack = False
            break
            

"""
    A GRAPH TO TEST THE ALGORITHM
"""

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

DFS(graph, "Z", "A")
