def productSum(array, multiplier = 1):
    sumProd = 0
    for element in array:
        if type(element) is list:
            sumProd += productSum(element, multiplier + 1)
        else:
            sumProd += element
    return sumProd * multiplier

# Time Complexity: O(n) where n is the total number of elements in the array including sub-elements
# Space Complexity: O(d) where d is the greatest depth of 'special' arrays in the array