from collections import deque
class Node(object):
    def __init__(self, data, previous=None, nextNode=None):
        self.data = data
        self.previous = previous
        self.nextNode = nextNode
class SingleLinkNode(object):
    def __init__(self, data,  nextNode=None):
        self.data = data
        self.nextNode = nextNode
class LinkedList(object):
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
        node = SingleLinkNode(data)
        if self.head == None:
            self.head = node
        if self.tail != None:
            self.tail.nextNode = node
        self.tail = node
    def kth_to_last(self,k):
        if k < 1:
            return None
        buffer = deque()
        current = self.head
        for i in range(k):
            buffer.appendleft(current.data)
            if current.nextNode == None:
                if i == k-1:
                    return current.data
                else:
                    print "Linked list has fewer that k elements"
                    return None
            current = current.nextNode
        while current != None:
            buffer.appendleft(current.data)
            buffer.pop()
            current = current.nextNode
        return buffer.pop()
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

    def sumLists(self,List):
        if List  == None:
            return None
        carry = 0
        sumList = DoubleLinkedList()
        Lp = List.head
        selfp = self.head
        while (Lp != None and selfp != None):
            sum = Lp.data + selfp.data + carry
            if sum >9:
                carry = 1
                sum %= 10
            else:
                carry = 0
            sumList.addData(sum)
            Lp = Lp.nextNode
            selfp = selfp.nextNode
        for ptr in (Lp,selfp):  # one of the numbers is longer than the other
            while ptr != None:
                sum = ptr.data + carry
                if sum >9:
                    carry = 1
                    sum %= 10
                else:
                    carry = 0
                sumList.addData(sum)
                ptr = ptr.nextNode
            if carry ==1:
                sumList.addData(carry)
                carry = 0
        return sumList
def remove_dups(l):
    current = l.head
    values = dict()
    while current != None:
        if current.data not in values:
            values[current.data] = 1
        else:
            current.previous.nextNode = current.nextNode
        current = current.nextNode
def remove_dups_no_buffering(l):
    if l.head == l.tail:
        return
    current = l.head
    while current != None:
        upstream = current.nextNode
        while upstream != None:
            if upstream.data == current.data:
                upstream.previous.nextNode = upstream.nextNode
            upstream = upstream.nextNode
        current = current.nextNode
def isPalindrome(head,tail):
    if head == tail:
        return True   #single element palindrome
    if head.data != tail.data:
        return False
    if head.nextNode == tail:
        return True   #two element list both equal
    return isPalindrome(head.nextNode,tail.previous)


if __name__ == '__main__':
    number1 = DoubleLinkedList(Node(7))
    number1.addData(1)
    number1.addData(7)
    print number1
    number2 = DoubleLinkedList()
    number2.addData(9)
    number2.addData(9)
    number2.addData(9)
    print number2
    print number1.sumLists(number2)
    remove_dups(number1)
    print number1
    tests = [[3],[1,1],[1,2],[1,2,3,3,2,1],[1,2,3,1,4,5,2,6]]
    def makelists(inputs):
        linkedLists = []
        for each in inputs:
            L = DoubleLinkedList()
            for item in each:
                L.addData(item)
            linkedLists.append(L)
        return linkedLists
    lists = makelists(tests)
    for l in lists:
        print l
        print isPalindrome(l.head,l.tail)
    remove_dups_no_buffering(lists[-1])
    print lists[-1]
    single_linked_list = LinkedList()
    for i in [10,9,8,7,6,5,4,3,2,1]:
        single_linked_list.addData(i)
    print single_linked_list
    print single_linked_list.kth_to_last(3)
    print single_linked_list.kth_to_last(5)
    print single_linked_list.kth_to_last(0)
    print single_linked_list.kth_to_last(13)
