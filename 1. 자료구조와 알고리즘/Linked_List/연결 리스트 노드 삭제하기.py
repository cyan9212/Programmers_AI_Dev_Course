class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        
        cur = self.getAt(pos)
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            
        if pos == 1:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            
        elif pos == self.nodeCount:
            prev = self.getAt(pos-1)
            prev.next = None
            self.tail = prev
            
        else:
            prev = self.getAt(pos-1)
            nex = self.getAt(pos+1)
            prev.next = nex
        
        self.nodeCount-=1
        
        return cur.data
    
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
