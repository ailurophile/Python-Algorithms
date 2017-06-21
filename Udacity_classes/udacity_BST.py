class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        out =  str(self.value)
        if self.left != None:
            out = out + " left: "+ str(self.left.value)
        if self.right != None:
            out = out + " right: "+ str(self.right.value)
        return out

class BST(object):
    def __init__(self, root):
        if isinstance(root, Node) :
            self.root = root
        else:
            self.root = Node(root)

    def __str__(self):
        if self.root == None:
            return "Empty tree!"
        node_values = []
        self.preorder_print(self.root, node_values)
        return ' '.join(str(value) for value in node_values)

    def preorder_print(self, start, traversal):
        if start == None:
            return
        traversal.append(start.value)
        self.preorder_print(start.left, traversal)
        self.preorder_print(start.right, traversal)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.search_from_node(self.root, find_val)

    def search_from_node(self, start, find_val):
        if start == None:
            return False
        if start.value == find_val:
            return True
        if start.value > find_val:
            return self.search_from_node(start.left, find_val)
        return self.search_from_node(start.right, find_val)

    def insert(self, value):
        if isinstance(value, Node):
            return self.insert_node( self.root, value)
        else:
            return self.insert_value( self.root, value)

    def insert_value(self, start, value):
        if start == None:
            start = Node(value)
            return
        if value <= start.value:
            if start.left == None:
                start.left = Node(value)
                return
            else:
                return self.insert_value(start.left, value)
        elif start.right == None:
            start.right = Node(value)
            return
        else:
            return self.insert_value(start.right, value)

    def insert_node(self, start, node):
        if start == None:
            start = node
            return
        if node.value <= start.value:
            if start.left == None:
                start.left = node
                return
            else:
                return self.insert_node(start.left, node)
        elif start.right == None:
            start.right = node
            return
        else:
            return self.insert_node(start.right, node)
    def print_nodes(self):
        nodes = []
        self.get_nodes(self.root, nodes)
        for node in nodes:
            print node
    def get_nodes(self, start, nodes):
        if start == None:
            return
        nodes.append(start)
        self.get_nodes(start.left, nodes)
        self.get_nodes(start.right, nodes)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(13)
    node4 = Node(14)
    node5 = Node(5)
    node6 = Node(3)

    tree = BST(node3)
    tree2 = BST(3)
    tree2.root.left = Node(66)
#    tree2.root.right = node4
#    node4.right = Node(99)
    node3.left = node2
#    tree.root.left = node2
    node2.left = node1
    tree.root.right = node4
    print tree
    print tree2
    print node3
    print tree.search(1)
    print tree.search(4)
    print tree.search(6)
    tree.insert(12)
    print tree
    tree.insert(15)
    print tree
    tree.insert(node5)
    print tree
    tree.print_nodes()
    print tree.insert(node6)
    print tree

#
