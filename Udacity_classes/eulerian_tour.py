def edge(ends):
    return (ends) if ends[0] < ends[1] else (ends[1], ends[0])
def get_next(node, graph):
    for index, leg in enumerate(graph):
        if node in leg:
            graph.pop(index)
            if node == leg[0]:
                return leg[1]
            return leg[0]
#        else :print node," not found, graph = ", graph
    else: return None
    
def find_eulerian_tour(graph):
    unconnected = []
    tour = []
    
    for e in graph:
        unconnected.append(e)

    leg = unconnected.pop()
    first = leg[0]
    current = leg[1]
    loops = []
    tour.append(first)
    tour.append(current)
    while unconnected:
        current = get_next(current, unconnected)
        if current != None:    # path continues
            tour.append(current)
        elif tour[0] != tour[-1]:  # not a tour
                return None
                
        else:
            loop = find_eulerian_tour(unconnected)
            if loop == None:
                return None
            else:
                loops.append(loop)
    if loops:
        print "loops = ", loops
                  
                
                

                
            
            
    return tour

#    print unconnected


def test():
#    print find_eulerian_tour([(1,2),(3,2),(3,1)])
#    print find_eulerian_tour([(1,2),(3,2),(3,4),(4,5),(5,2),(4,2),(4,1)])
    print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print find_eulerian_tour([(1,2),(3,2),(3,1),(2,2)])
    
