#Approach 1
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

#Time Complexity: O(n^2)
#Space Complexity: O(1)

###################################

#Approach 2
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        if targetSum-num in nums:
            return [targetSum-num, num]
        else:
            nums[num]= True
    return []

#Time Complexity: O(n)
#Space Complexity: O(n)

#####################################

#Approach 3
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while(left<right):
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right-= 1
        elif currentSum < targetSum:
            left+= 1
    return []

#Time Complexity: O(nlogn)
#Space Complexity: O(1)