#Approach 1: Recursive
def binarySearchRec(array, target):
    return binarySearchRecHelper(array, target, 0 ,len(array)-1)

def binarySearchRecHelper(array, target, left, right):
    if left>right:
        return -1
    middle = (left + right )//2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return binarySearchRecHelper(array, target, left, middle-1)
    else:
        return binarySearchRecHelper(array, target, middle+1 , right)

#Time Complexity: O(logn)
#Space Complexity: O(logn)

###################################

#Approach 2: Iterative
def binarySearchIter(array, target):
    return binarySearchIterHelper(array, target, 0 ,len(array)-1)

def binarySearchIterHelper(array, target, left, right):
    while left<=right:
        middle = (left + right)//2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle-1
        else:
            left = middle +1
    return -1

#Time Complexity: O(logn)
#Space Complexity: O(1)