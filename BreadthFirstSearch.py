#BreadthFirstSearch.py
#by YesayaYova
#with Python3

"""
    BREADTH FIRST SEARCH ALGORITHM
    with input is a graph
"""

def BFS(graph, goal, first):
    explored = [first]
    queue    = []
    current  = first
    
    while True:        
        #if goal was found
        if current == goal:
            print ("\nFound!")
            break
        
        #check on each current's neighbour 
        for neighbour in graph[current]:
            if neighbour not in explored: 
                queue.append(neighbour)
        
        print(current, end=" ")
        explored.append(current)
        current = queue.pop(0)
        
        #if goal wasn't found
        if len(queue) == 0:
            print(". . .\nNot Found!")
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

BFS(graph, "Z", "A")
