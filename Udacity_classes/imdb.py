import csv
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = []
    top20 = []
    for i in range(20):
        top20.append(["dummy", 10000000])
    lines = 0
#    for line in tsv: print line
    for (actor,movie,date) in tsv:
        make_link(G, actor, movie+date)
        if actor not in actors:
            actors.append(actor)
    for star in actors:
        c = centrality(G,star)
        if c >= top20[19][1]: continue
        for j in range(20):
            if c < top20[j][1]:
                for k in range(19,j,-1):  #would have been more efficient to K-partition
                    top20[k] = top20[k-1]
                top20[j] =[star,c]
                break
                    


    return top20

def test():
    G = read_graph("imdb-1.tsv")
    print G

test()
