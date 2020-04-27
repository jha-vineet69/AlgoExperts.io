class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchHelper(root, sums=None, branchSum=0):
    if root is None:
        return

    if sums is None:
        sums = []

    branchSum += root.value
    if root.left is None and root.right is None:
        sums.append(branchSum)

    branchHelper(root.left, sums, branchSum)
    branchHelper(root.right, sums, branchSum)
    return sums

def branchSums(root):
    return branchHelper(root) 

#Time Complexity: O(nlogn)
#Space Complexity: O(n)

