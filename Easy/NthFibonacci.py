#Approach 1: Recursive 
def getNthFibRec(n):
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

# Time Complexity = O(2^n)
# Space Complexity = O(n)

#############################

#Approach 2: Memoization
def getNthFibMem(n, memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    
    else:
        memoize[n] = getNthFibMem(n-1, memoize) + getNthFibMem(n-2, memoize)
        return memoize[n]
    
# Time Complexity = O(n)
# Space Complexity = O(n)

#############################

#Approach 3: Iterative
def getNthFibIter(n):
    lastTwo = [0,1]
    counter = 3
    while counter<=n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n>1 else lastTwo[0]

# Time Complexity = O(n)
# Space Complexity = O(1)


    