#BreadthFirstSearch.py
#oleh YesayaYova
#dengan Python3

"""
    BREADTH FIRST SEARCH ALGORITHM
    dengan inputan berupa sebuah graph
"""

def BFS(graph, goal, first):
    explored = [first]
    queue    = []
    current  = first
    
    while True:        
        #jika goal state ditemukan
        if current == goal:
            break
            
        #mengecek disetiap neighbour dari current state 
        for neighbour in graph[current]:
            if (neighbour[0] not in explored) and (neighbour[0] not in queue): 
                queue.append(neighbour[0])
        
        print(current)
        
        #mengecek pada state yang telah dilewati
        if current not in explored:
            explored.append(current)
        current = queue.pop(0)
        
        #jika goal state tidak ditemukan
        if len(queue) == 0:
            break
        
    if current == goal:
        print(goal, "Found!")
    else:
        print("Not Found!")
