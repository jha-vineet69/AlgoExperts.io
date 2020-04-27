#Approach 1
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString+= string[i] #Takes O(n) time
    return string == reversedString

#Time Complexity: O(n^2)
#Space Complexity: O(n)

###################################

#Approach 2
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i]) #Takes O(1) time
    return string == "".join(reversedChars)

#Time Complexity: O(n)
#Space Complexity: O(n)

###################################

#Approach 3
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    if i>= j:
        return True
    else:
        return string[i] == string[j] and isPalindrome(string, i+1)

#Time Complexity: O(n)
#Space Complexity: O(n)

###################################

#Approach 4
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left]!=string[right]:
            return False
        left+=1
        right-=1
    return True

#Time Complexity: O(n)
#Space Complexity: O(1)

