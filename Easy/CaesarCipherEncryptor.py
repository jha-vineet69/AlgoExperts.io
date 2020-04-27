#Approach 1 : This solution needs you to know ASCII/Unicode values of the alphabets
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return ".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    if newLetterCode <=122:
        return chr(newLetterCode)
    else:
        return chr(96 + newLetterCode % 122)

#Time Complexity: O(n)
#Space Complexity: O(n)

###################################

#Approach 2
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return ".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    if newLetterCode <=25:
        return alphabet[newLetterCode]
    else:
        return alphabet[-1 + newLetterCode % 25]

#Time Complexity: O(n)
#Space Complexity: O(n)

