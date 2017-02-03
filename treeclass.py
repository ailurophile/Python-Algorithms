def make_link(G,node1,node2):
    if node1 not in G:
        G[node1]={}
    if node2 not in G:
        G[node2]={}
    (G[node1])[node2]=1
    return G
def route_between(G, node1, node2):
    marked = {}
    openList = [node1]
    while len(openList)>0:
        currentNode = openList.pop(0)
        for neighbor in G[currentNode].keys():
            if neighbor == node2 : return True
            if neighbor not in marked:
                marked[neighbor]=True
                openList.append(neighbor)
    return False

class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left=left
        self.right=right
    #def __str__(self):
    def displayall(self):
        output = []
        openList = [self]
        while len(openList)>0:
            currentNode = openList.pop(0)
            output.append(currentNode.data)
            if currentNode.left != None:
                openList.append(currentNode.left)
            if currentNode.right != None:
                openList.append(currentNode.right)
        return str(output)
    def __str__(self):
        out =  str(self.data)
        if self.left != None:
            out = out + " left: "+ str(self.left.data)
        if self.right != None:
            out = out + " right: "+ str(self.right.data)
        return out
class Tree(object):
    def __init__(self, root):
        self.root = Node(root)
    def __getattr__(self, attr):
        return getattr(self.root, attr)
    def __str__(self):
        output = []
        openList = [self.root]
        while len(openList)>0:
            currentNode = openList.pop(0)
            output.append(currentNode.data)
            if currentNode.left != None:
                openList.append(currentNode.left)
            if currentNode.right != None:
                openList.append(currentNode.right)
        return str(output)
    
    """
     def __str__(self):
        if self.root != None:
            return self.root.displayall()
        return ''
       
        output = []
        openList = [self.root]
        while len(openList)>0:
            currentNode = openList.pop(0)
            output.append(currentNode.data)
            if currentNode.left != None:
                openList.append(currentNode.left)
            if currentNode.right != None:
                openList.append(currentNode.right)
               
        #print output
      
        return str(output)
    """
def makeBinarySearchTree(inputList):
    length = len(inputList)
    if length == 0:
        return None
    if length == 1:
        return Node(inputList[0])
    middle = length/2
    root = Node(inputList[middle])
    #print root.data
    root.left = makeBinarySearchTree(inputList[:middle])
    root.right = makeBinarySearchTree(inputList[middle+1:])
    return Tree(root)
    
if __name__ == '__main__':
    G = {}
    links = [(1,2),(2,3),(2,0),(4,3)]
    for (x,y) in links:
        G = make_link(G,x,y)
    print route_between(G,1,3)
    print route_between(G,1,4)
    G = make_link(G,0,4)
    print route_between(G,1,4)
    print G
    arrays = [[0],[1,2],[1,2,3,4,5,6,7],[1,2,3,4,5,6]]  
    for array in arrays:
        BinaryTree = makeBinarySearchTree(array)
        print array
        #print type(BinaryTree)
        print BinaryTree.displayall()
        #print BinaryTree