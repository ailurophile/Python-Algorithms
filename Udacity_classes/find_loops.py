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
def find_loop(unconnected):
    leg = unconnected.pop()
    first = leg[0]
    current = leg[1]
    tour = []
    tour.append(first)
    tour.append(current)
    while unconnected:
        current = get_next(current, unconnected)
#        print "tour = ", tour," current = ", current," unconnected = ", unconnected
        if current != None:    # path continues
            tour.append(current)
        elif first == tour[-1]:
            return tour
        else:
            return None
    return tour
def merge_loops(short1,short2,common):
    longLoop = [common]
    index = short1.index(common)
    for i in range (index + 1,len(short1)):
        longLoop.append(short1[i])
    for i in range (1,index+1):
        longLoop.append(short1[i])
    index = short2.index(common)
    for i in range (index + 1, len(short2)):
        longLoop.append(short2[i])
    for i in range (1, index+1):
        longLoop.append(short2[i])
    return longLoop
   
def find_eulerian_tour(graph):
    unconnected = []
    loops = []
    
    for e in graph:
        unconnected.append(e)
        
    while unconnected:
        loop = find_loop(unconnected)
#        print "loop = ", loop
        if loop == None:
            return None
        else:
            loops.append(loop)
    numLoops = len(loops)
    if numLoops == 1:
        return loops[0]
    else:
        pivot = None
        tries = 1
        while tries < numLoops:
            loop1 = loops.pop(0)
            for node in loop1:
                for i in range (0, len(loops)):
                    if node in loops[i]:
                        pivot = node
                        break
            if pivot != None:
                tries = numLoops
            else:
                tries = tries + 1
                loops.append(loop1)
            
        print "pivot = ", pivot,"loop1 = ", loop1,"loops[i] = ", loops[i]
        longLoop = merge_loops(loop1,loops.pop(i),pivot)
        loops.append(longLoop)
                
                  
                
                

                
            
            
    return loops[0]

#    print unconnected


def test():
    print find_eulerian_tour([(1,2),(3,2),(3,1)])
    print find_eulerian_tour([(1,2),(3,2),(3,4),(4,5),(5,2),(4,2),(4,1)])
#    print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print find_eulerian_tour([(1,2),(3,2),(3,1),(2,2)])
    
