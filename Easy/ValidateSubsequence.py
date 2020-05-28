def validateSubsequence(arr, sequence):
    seqIdx=0
    for val in arr:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == val:
            seqIdx+=1
    return seqIdx == len(sequence)


#Time Complexity: O(n)
#Space Complexity: O(1)

###################################