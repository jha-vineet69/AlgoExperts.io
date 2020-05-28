def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)


#Time Complexity: O(n)
#Space Complexity: O(h)

###################################