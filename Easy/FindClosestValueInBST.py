#Approach 1 : Recursive
def findClosestValueInBst(tree, target):
    return helper(tree, target, float("inf"))


def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target-tree.value):
        closest = tree.value
    if target < tree.value:
        return helper(tree.left, target, closest)
    elif target > tree.value:
        return helper(tree.right, target, closest)
    else:
        return closest
    
#Average:
#Time Complexity: O(logn)
#Space Complexity: O(logn) [Because of Recursive Call Stack]
#Worst: (When there is no branching and just a linear chain)
#Time Complexity: O(n)
#Space Complexity: O(n)

##################################################

#Approach 2 : Iterative
def findClosestValueInBst(tree, target):
    return helper(tree, target, float("inf"))


def helper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
        return closest
    
#Average:
#Time Complexity: O(logn)
#Space Complexity: O(1)
#Worst: (When there is no branching and just a linear chain)
#Time Complexity: O(n)
#Space Complexity: O(1)