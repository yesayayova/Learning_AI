#BestFirstSeach.py
#oleh Yesaya Yova
#dengan Python3

def BestFirstSearch(graph, heuristik, goal, start):
    current  = start
    explored = [start]
    
    while True:
        frontier = []
        
        #jika goal-state ditemukan
        if current == goal:
            print(explored)
            break
        
        #mengecek seluruh child dari goal-state
        for i in range(len(graph[current])):
            frontier.append(graph[current][i][0])
        
        #jika goal-state tidak ditemukan
        if len(frontier) == 0:
            print("Not Found")
            break
        
        #memilih suksesor dengan fungsi heuristik tererndah
        x = frontier[0]
        for i in frontier:
            if heuristik[i] < heuristik[x]:
                x = i
                
        explored.append(x)
        current = x
