class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    
#Average:
#Time Complexity: O(V + E)
#Space Complexity: O(V) [Because of length of array we return]
#Worst: (When there is no branching and just a linear chain)
#Time Complexity: O(V)
#Space Complexity: O(V)