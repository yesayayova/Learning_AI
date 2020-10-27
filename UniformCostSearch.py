#Algoritma Uniform Cost Search
#oleh Yesaya Yova
#dengan Python3

def uniform(graph, goal, start):   
    frontier        = [start]
    frontier_cost   = [0]
    frontier_route  = [[start]]
    explored        = []
    goal            = goal
    
    while True:
        #Jika goal tidak ditemukan
        if len(frontier) == 0:
            print("Not find")
            break
            
        current_cost  = frontier_cost.pop(0)
        current_state = frontier.pop(0)
        current_route = frontier_route.pop(0)
        
        #Jika goal ditemukan
        if current_state == goal:
            print(current_route)
            break
        
        #mengecek pada setiap child current_state
        for i in range(len(graph[current_state])):
            if i not in explored:
                #menambahkan state baru ke frontier
                frontier.append(graph[current_state][i][0])
                
                #menambahkan daftar harga tiap rute baru ke frontier_cost
                frontier_cost.append(current_cost+graph[current_state][i][1])
                
                #menambahkan rute baru ke frontier_route
                x = current_route.copy()
                x.append(graph[current_state][i][0])
                frontier_route.append(x)
                
        #melakukan sortir secara ascending
        sort(frontier, frontier_cost, frontier_route)

#fungsi untuk mengsortir secara ascending
def sort(frontier, frontier_cost, frontier_route):
    for i in range(1, len(frontier)):
        key  = frontier_cost[i]
        key2 = frontier[i]
        key3 = frontier_route[i]
        j = i - 1
        while j >= 0 and frontier_cost[j] > key:
            frontier_cost [j+1] = frontier_cost[j]
            frontier [j+1]      = frontier [j]
            frontier_route[j+1] = frontier_route[j]
            j = j - 1
        frontier_route[j+1] = key3
        frontier[j+1]       = key2
        frontier_cost[j+1]  = key
