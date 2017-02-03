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

def getstrongest(C):
    max_strength = 0
    pair = ('','')
    return max((strength, guy1, guy2) for guy1, connection in C.items() for guy2,
               strength in connection.items())
def test():
    G,H = read_graph("marvel.tsv")
    print getstrongest(H)
#    print G

test()
