import csv
from collections import defaultdict
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = defaultdict(int)
    (G[node1])[node2] += 1
    if node2 not in G:
        G[node2] = defaultdict(int)
    (G[node2])[node1] += 1
    return G

import heapq
def getshortest(G, v1):
    path_from_start = {} 
    open_list = [v1]
    path_from_start[v1] = [v1] 
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: 
                path_from_start[neighbor] = path_from_start[current]+[neighbor] 
                open_list.append(neighbor)
    return path_from_start

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}              
    H = {}
               
    comics = set()
               
    for (node1, node2) in tsv:
        make_link(G, node1, node2)
        comics.add(node2)
    for comic in comics:
#        make_link(H, guy1, guy2) for guy1 in G[comic] for guy2 in G[comic]
        for guy1 in G[comic]:
            for guy2 in G[comic]:
                if guy1 != guy2:
                    make_link(H, guy1, guy2) 
                   
    return G,H
def getcheapest(G,v):
    dist_so_far = {}
    path_so_far = {v:[v]}
    dist_so_far[v] = [1,v]
    heap = []
    heapq.heappush(heap,dist_so_far[v])
    final_dist = {}
    final_path = {}
    while heap:
        entry = heapq.heappop(heap)
#        print "entry = ", entry
        node = entry[1]
        distance = entry[0]
        if node == "REMOVED": continue
        # lock it down!
        final_dist[node] = distance
        final_path[node] = path_so_far[node]
        del dist_so_far[node]
        for x in G[node]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = [final_dist[node] + (1.0/G[node][x]),x]
                    path_so_far[x] = path_so_far[node]+[x]
                    heapq.heappush(heap,dist_so_far[x])
                elif((final_dist[node] + 1.0/G[node][x]) < dist_so_far[x][0]):
                    dist_so_far[x][1] = "REMOVED"   #invalidate old heap entry
                    dist_so_far[x] = [final_dist[node] + (1.0/G[node][x]), x]
                    path_so_far[x] = path_so_far[node] + [x]
                    heapq.heappush(heap,dist_so_far[x])
#    return final_path
                elif ((final_dist[node]+1.0/G[node][x])==dist_so_far[x][0]):
                    if len(path_so_far[node])+1 <len(path_so_far[x]):
                        path_so_far[x] = path_so_far[node] + [x]
    return final_path

def getstrongest(C):
    max_strength = 0
    pair = ('','')
    return max((strength, guy1, guy2) for guy1, connection in C.items() for guy2,
               strength in connection.items())
def test():
    G,H = read_graph("marvel.tsv")
    characters = ['SPIDER-MAN/PETER PAR','GREEN GOBLIN/NORMAN ','WOLVERINE/LOGAN ',
                  'PROFESSOR X/CHARLES ', 'CAPTAIN AMERICA']
    U = {}
    W = {}
    D = defaultdict(int)  #path differences by character  Char:differences
    for character in characters:
        U[character] = getshortest(H,character)
        W[character] = getcheapest(H,character)
        for pal in H:
            if not pal in U[character]:
                continue
            if len(U[character][pal]) != len(W[character][pal]):
                D[character] += 1
                                    
#    print getstrongest(H)
    print D.items()," sum = ", sum(D.values())

test()
