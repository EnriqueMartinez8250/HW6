##Enrique Martinez-Acevedo

## Sources https://www.youtube.com/watch?v=IG1QioWSXRI

## https://pastebin.com/3Q9rqGHA

## https://www.youtube.com/watch?v=OrJ004Wid4o&t=1353s


graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 3, 'D': 2, 'E': 3},
        'C': {'B': 1, 'D': 4, 'E': 5},
        'D': {'E': 1},
        'E': {'F': 7},
        'F': {'G': 8, 'H': 6},
        'G': {'H': 1},
        'H': {}
    }



def dijkstra_with_output(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph.copy()
    infinity = 9999999 #infinity 
    path = []
    

    ##Sets the shortest distance for all nodes as infinity
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    while unseenNodes:
        minNode = None
        
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        print("\nNode", minNode, "with weight:", shortest_distance[minNode],"is added to the 'Visited' ") ##Added Personally 
##########################################################################################################################################        
        for childNode, weight in graph[minNode].items():
            old_cost = shortest_distance[childNode]
            new_cost = weight + shortest_distance[minNode]
            if new_cost < old_cost:
                print("\tRelaxed: vertex", childNode, ": OLD:", old_cost, "NEW:", new_cost, "Paths:", predecessor) ##Added personally
                shortest_distance[childNode] = new_cost
                predecessor[childNode] = minNode
            else:
                print("\tNo edge relation is needed for node: ", childNode)    
        unseenNodes.pop(minNode)

#############################################################################################################################################    
    
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))
    
    return shortest_distance, predecessor


def main():
    print("Algorithms homework #6")
    user_selection = int(input("1. Run program\n2. Exit\nSelection: "))
    if(user_selection == 1):
        dijkstra_with_output(graph, 'A', 'E')
    if(user_selection == 2):
        print("Exiting...")
        return 
main()


