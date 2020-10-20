#DepthFirstSearch.py
#oleh YesayaYova
#dengan Python3

"""
    DEPTH FIRST SEARCH ALGORITHM
    dengan inputan berupa sebuah graph
"""

def DFS(graph, goal, first):
    explored = [first]
    queue    = []
    current  = first
    
    while True:        
        #jika goal state ditemukan
        if current == goal:
            break
        
        #mengecek setiap neighbour pada current state
        for neighbour in graph[current]:
            if (neighbour[0] not in explored)and (neighbour[0] not in queue): 
                queue.append(neighbour[0])
        
        
        print(current)
        #mengecek pada explored
        if current not in explored:
            explored.append(current)
        
        #mengambil suksesor dengan prinsip LIFO
        current = queue.pop()
        
        #jika goal state tidak ditemukan
        if len(queue) == 0:
            break
        
    if current == goal:
        print(goal, "Found!")
    else:
        print("Not Found!")
