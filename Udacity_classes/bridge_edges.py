# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       
def create_rooted_spanning_tree(G, root):
    S = {}
    # your code here
    S[root] = {}
#    depth = {root:0}
    open_list = [root]
    
    while len(open_list) > 0:
        current = open_list.pop()
        for node in G[current]:
            if node not in S:
                open_list.append(node)
                S[node] = {current:"green"}
                S[current][node] = "green"
#                depth[node] = depth[current] + 1
            elif node not in S[current]:
                S[node][current] = "red"
                S[current][node] = "red"
#    print depth
                        
    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    
    print S

    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'green'}, 
                 'c': {'a': 'green', 'd': 'red'}, 
                 'd': {'c': 'red', 'b': 'green', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    # your code here
    depth = {root:0}
    open_list = [root]
    maxDepth = 0
    
    while len(open_list) > 0:
        current = open_list.pop()
        for node in S[current]:
            if node not in depth:
                open_list.append(node)
                depth[node] = depth[current] + 1
                if depth[node] > maxDepth:
                    maxDepth = depth[node]
                    leaf = node  
    po = {leaf:1}
    last = leaf
    nodeNum = 2
    while root not in po:
        if len(open_list) > 0:
            current = open_list.pop()
        else:
            for node in S[last]:  #find parent of last node
                if S[node][last] == "green" and depth[node] == depth[last]-1:
                    current = node
        while True:
            deeper = [n for n, c in S[current].items() if (c == "green" and n not in po and depth[n]>depth[current])]
            if deeper:
                open_list.append(deeper[0])
                current = deeper[0]
            elif len(open_list)>0:  #more children found
                last = open_list.pop()
                po[last] = nodeNum
                nodeNum += 1
                break   #find parent of numbered node
            else:       #node is a leaf
                po[current] = nodeNum
                nodeNum += 1
                last = current
                break   #find parent of numbered node                                    
                    
#    print depth, "leaf =", leaf
    return po
    
#    pass


def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    print "post order = ", po
    assert po == {'a':7, 'b':6, 'c':5, 'd':4, 'e':3, 'f':2, 'g':1}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    depth = {root:0}
    open_list = [root]
    maxDepth = 0
    
    while len(open_list) > 0:
        current = open_list.pop()
        for node in S[current]:
            if node not in depth:
                open_list.append(node)
                depth[node] = depth[current] + 1
                if depth[node] > maxDepth:
                    maxDepth = depth[node]
#                    leaf = node  
    desc = {}
    leaves = [n for n,d in depth.items() if d == maxDepth]
    for node in leaves:
        desc[node] = 1
    nextLevel = maxDepth - 1
    while nextLevel >= 0:
        levelNodes = [n for n,d in depth.items() if d == nextLevel]
        
        for node in levelNodes:
            desc[node] = 1 + sum([desc[n] for n,c in S[node].items() if c == "green" and n in desc])
        nextLevel = nextLevel - 1
    return desc
                                  

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    print "descendants = ", nd
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    depth = {root:0}
    open_list = [root]
    maxDepth = 0
    while len(open_list) > 0:
        current = open_list.pop()
        for node in S[current]:
            if node not in depth:
                open_list.append(node)
                depth[node] = depth[current] + 1
                if depth[node] > maxDepth:
                    maxDepth = depth[node]
    lpo = {}
    nextLevel = maxDepth
    while nextLevel >= 0:
        leaves = [n for n,d in depth.items() if d == nextLevel]
        for node in leaves:
            minpo = po[node]
            for neighbor in S[node]:
                if neighbor in lpo:
                    minpo = min(minpo, lpo[neighbor])
                else:
                    minpo = min(minpo, po[neighbor])
            lpo[node] = minpo
        nextLevel = nextLevel - 1
    return lpo
        
                                
         
            
            


def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    print "S = ", S
    print "lowest post orders = ", l
#    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':1, 'f':1, 'g':1}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    depth = {root:0}
    open_list = [root]
    maxDepth = 0
    while len(open_list) > 0:
        current = open_list.pop()
        for node in S[current]:
            if node not in depth:
                open_list.append(node)
                depth[node] = depth[current] + 1
                if depth[node] > maxDepth:
                    maxDepth = depth[node]
    hpo = {}
    nextLevel = maxDepth
    while nextLevel >= 0:
        leaves = [n for n,d in depth.items() if d == nextLevel]
        for node in leaves:
            maxpo = po[node]
            for neighbor in S[node]:
                if neighbor in hpo:
                    maxpo = max(maxpo, hpo[neighbor])
                elif S[node][neighbor] == "red" or depth[neighbor] > depth[node]:
                    maxpo = max(maxpo, po[neighbor])
            hpo[node] = maxpo
        nextLevel = nextLevel - 1
    return hpo
def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    print "highest post order = ", h
#    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    assert h == {'a':7, 'b':6, 'c':6, 'd':6, 'e':3, 'f':2, 'g':2}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    l = lowest_post_order(S, root, po)
    h = highest_post_order(S, root, po)
#    print "S = ", S
#    print " post order = ", po
#    print "number of descendants =", nd
#    print "lowest post order =", l
#    print "highest post order =", h    
    bridges = []
    candidates = [node for node in S if h[node] <= po[node]]
#    print "candidates = ", candidates
    possibles = [node for node in candidates if l[node] > (po[node] - nd[node])]
#    print "possibles = ", possibles
    for each in possibles:
        for node in S[each]:
            if S[node][each] == "green" and po[node] > po[each]:
                bridges. append((node,each))
    return bridges

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')

#    print "bridges = ", bridges
    assert bridges == [('d', 'e')]
#test_create_rooted_spanning_tree()
#test_post_order()
#test_number_of_descendants()
#test_lowest_post_order()
#test_highest_post_order()
test_bridge_edges()