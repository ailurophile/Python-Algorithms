MAX_TREE_DEPTH = 100
#import math

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

class TreeNode(object):
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
def makeBinarySearchTree(inputList):
    length = len(inputList)
    if length == 0:
        return None
    if length == 1:
        return TreeNode(inputList[0])
    middle = length/2
    root = TreeNode(inputList[middle])
    #print root.data
    root.left = makeBinarySearchTree(inputList[:middle])
    root.right = makeBinarySearchTree(inputList[middle+1:])
    return root

class Node(object):
    def __init__(self, data, previous=None, nextNode=None):
        self.data = data
        self.previous = previous
        self.nextNode = None
        
class DoubleLinkedList(object):
    def __init__(self, head=None, tail = None):
        self.head = head
        if tail == None:
            self.tail = self.head
        else:
            self.tail = tail
        
    def __str__(self):
        out = []
        if self.head == None: return''
        ptr = self.head
        while ptr.nextNode != None:
            out.append(str(ptr.data)+'->')
            ptr = ptr.nextNode
        out.append(ptr.data)
        return str(out)
    
    def addData(self,data):
        node = Node(data,self.tail)
        if self.head == None:
            self.head = node
        if self.tail != None:
            self.tail.nextNode = node
        self.tail = node
def linkedListsTreeLevels(root):
    powerOfTwo = (2**i for i in range(MAX_TREE_DEPTH))
    outputLists = []
    
    levelCount = next(powerOfTwo)
    openList = [root]
    output = DoubleLinkedList()
    while len(openList) > 0:        
        currentNode = openList.pop(0)        
        if currentNode.left != None:
            openList.append(currentNode.left)
        if currentNode.right != None:
            openList.append(currentNode.right)
        output.addData(currentNode.data)
        #print output
        levelCount -= 1
        if levelCount == 0 or len(openList) == 0:
            levelCount = next(powerOfTwo)
            outputLists.append(output)
            output = DoubleLinkedList()
    return outputLists
def depth(pair): return pair[0]
def balanced(pair): return pair[1]
def isBalanced(tree): return balanced(getDepth(tree))
def getDepth(tree):
    if tree.left == None:
        left_height = 0
        left_balanced = True
    else:
        left = getDepth(tree.left)
        left_height = depth(left) + 1
        left_balanced = balanced(left)
        
    if tree.right == None:
        right_height = 0
        right_balanced = True
    else:
        right = getDepth(tree.right)
        right_height = depth(right) + 1
        right_balanced = balanced(right)
        
    height = max(left_height, right_height)
    if left_balanced and right_balanced:
        return (height, abs(left_height - right_height) <2)
    return (height, False)
def isBST(tree, minVal=None, maxVal = None):
    if tree == None:
        return True
    if (isBST(tree.left,minVal,tree.data) and isBST(tree.right, tree.data, maxVal)) != True:
        return False
    return not(maxVal!=None and tree.data > maxVal) or (minVal!=None and tree.data <= minVal)
    """
    if (maxVal!=None and tree.data > maxVal) or (minVal!=None and tree.data <= minVal):
        return False
    return True
    """
previous = [None]
def inOrderIsBST(tree):
    if tree.left != None:
        if inOrderIsBST(tree.left) == False: return False
    print (tree.data)
    if tree.data < previous[0]:
        return False
    previous[0] = tree.data
    if tree.right != None:
        if inOrderIsBST(tree.right) == False: return False
    return True

def DFS(tree,n):
    if tree == None: return None
    processed = []
    openList = [tree]
    while len(openList) > 0:
        current = openList.pop()
        if current.data == n:
            return True
        if current.left != None and current.left not in processed:
            openList.append(current.left)
        if current.right != None and current.right not in processed:
            openList.append(current.right)
    return False
# is currend node one of the children being sought?
def FCA(root,a,b):
    if root == None: 
        return None
    #print "root = %s" %root.data
    if (root.data == a) or (root.data == b): 
        return root.data
    if DFS(root.right,a):
        #print "a found right"
        if DFS(root.left,b):
            #print " b found left"
            return root.data
        if DFS(root.right,b):
            #print "b found right"
            if (root.right.data == a) or (root.right.data == b): #a&b descendants

                return root.data
            return FCA(root.right,a,b)
        else:
            return a       #b not in tree
    if DFS(root.left,a):
        #print "a found left"
        if DFS(root.right,b):
            #print "b found right"
            return root.data
        if DFS(root.left,b):
            #print "left = %s right = %s"% (root.left.data,root.right.data)
            if (root.left.data == a) or (root.left.data == b): #a&b descendants
                return root.data
            return FCA(root.left,a,b)
        else:
            return a       #b not in tree
    else:  #a not in tree
        if DFS(root, b):
            return b    
        else:
            return None
    
if __name__ == '__main__':
    
    
    tree = TreeNode(3)
    tree.left = TreeNode(2)
    tree.left.right = TreeNode(10)
    tree.right = TreeNode(8)
    print DFS(tree,3)
    print DFS(tree,4)
    print DFS(tree,10)
    bigTree = makeBinarySearchTree(range(15))
    print bigTree.displayall()
    print FCA(bigTree,0,2)
    print FCA(bigTree,10,9)
    print FCA(bigTree,4,11)
    print FCA(bigTree,5,2)
    print FCA(bigTree,12,13)
    """"
    print getDepth(tree)
    print isBST(tree)
    print inOrderIsBST(tree)
    
    number1 = DoubleLinkedList(Node(7))
    number1.addData(1)
    number1.addData(7)
    print number1
    G = {}
    links = [(1,2),(2,3),(2,0),(4,3)]
    for (x,y) in links:
        G = make_link(G,x,y)
    print route_between(G,1,3)
    print route_between(G,1,4)
    G = make_link(G,0,4)
    print route_between(G,1,4)
    print G
    arrays = [[0],[1,2],[1,2,3,4,5,6,7],[1,2,3,4,5,6],[1,2,3,4,5,6,7,8,9]]  
    arrays2 = [[1,2,3,4],[1,2,3]]
    for array in arrays:
        BinaryTree = makeBinarySearchTree(array)
        print array
        #print type(BinaryTree)
        print BinaryTree.displayall()
        tree = BinaryTree
        #print tree
        lists= linkedListsTreeLevels(tree)
        for l in lists:
            print l
       """     