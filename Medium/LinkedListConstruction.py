class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# Time Complexity: O(1)
# Space Complexity: O(1)    
    def setHead(self, node):
        if self.head is None:
            self.head = None
            self.tail = None
            return
        self.insertBefore(self.head, node)

        
# Time Complexity: O(1)
# Space Complexity: O(1)
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)


# Time Complexity: O(1)
# Space Complexity: O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


# Time Complexity: O(1)
# Space Complexity: O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

# Time Complexity: O(p)
# Space Complexity: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node and currentPosition!= position:
            node = node.next
            currentPosition+= 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


# Time Complexity: O(n)
# Space Complexity: O(1)
    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)


# Time Complexity: O(1)
# Space Complexity: O(1)
    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)


# Time Complexity: O(n)
# Space Complexity: O(1)
    def containsNodeWithValue(self, value):
        node = self.head
        while(node and node.value!= value):
            node = node.next
        return node!= None

# Time Complexity: O(1)
# Space Complexity: O(1)
    def removeNodeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
