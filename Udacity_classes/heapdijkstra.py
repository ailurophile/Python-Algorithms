
import heapq


def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = [0,v]
    heap = []
    heapq.heappush(heap,dist_so_far[v])
    final_dist = {}
    while len(final_dist) < len(G):
        entry = heapq.heappop(heap)
#        print "entry = ", entry
        node = entry[1]
        distance = entry[0]
        if node == "REMOVED": continue
        # lock it down!
        final_dist[node] = distance
        del dist_so_far[node]
        for x in G[node]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = [final_dist[node] + G[node][x],x]
                    heapq.heappush(heap,dist_so_far[x])
                elif final_dist[node] + G[node][x] < dist_so_far[x][0]:
                    dist_so_far[x][1] = "REMOVED"   #invalidate old heap entry
                    dist_so_far[x] = [final_dist[node] + G[node][x], x]
                    heapq.heappush(heap,dist_so_far[x])
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

test()   




