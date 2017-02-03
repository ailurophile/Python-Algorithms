#
# Modify long_and_simple_path 
# to build and return the path
# 

# Find me that path!
def long_and_simple_path(G,u,v,l):
    """
    G: Graph
    u: starting node
    v: ending node
    l: minimum length of path
    """
    if not long_and_simple_decision(G,u,v,l):
        print "original sin"
        return False
    # Otherwise, build and return the path
    path = [v]
    current = v
    l -= 1
    while current != u:
#        print "G[current] = ", G[current], "keys = ", G[current].keys()
    
        nodes = G[current].keys()
        remove_node(G,current)
        for neighbor in nodes:
            if  long_and_simple_decision(G,u,neighbor, l):
                if neighbor == u and l > 1:
                    continue
                path.append(neighbor)
                current = neighbor
                l -= 1
                break
    path.reverse()
    return path

def remove_node(G,node):
    if node not in G:
        print "error: removing nonexistent node"
        return
    links = G[node].keys()
    for neighbor in links:
        break_link(G,node,neighbor)
    assert len(G[node]) == 0
    G.pop(node)
#############

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def break_link(G, node1, node2):
    if node1 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G[node1]:
        print "error: breaking non-existent link"
        return
    if node1 not in G[node2]:
        print "error: breaking non-existent link"
        return
    del G[node1][node2]
    del G[node2][node1]
    return G

flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

def all_perms(seq):
    if len(seq) == 0: return [[]]
    if len(seq) == 1: return [seq, []]
    most = all_perms(seq[1:])
    first = seq[0]
    rest = []
    for perm in most:
        for i in range(len(perm)+1):
            rest.append(perm[0:i] + [first] + perm[i:])
    return most + rest

def check_path(G,path):
    for i in range(len(path)-1):
        if path[i+1] not in G[path[i]]: return False
    return True
    
def long_and_simple_decision(G,u,v,l):
    if l == 0:
        return False
    n = len(G)
    perms = all_perms(G.keys())
    for perm in perms:
        # check path
        if (len(perm) >= l and check_path(G,perm) and perm[0] == u 
            and perm[len(perm)-1] == v): 
            return True
    return False
def test():
    path = long_and_simple_path(G,1,6,4)
    print "path = ",path
test()
