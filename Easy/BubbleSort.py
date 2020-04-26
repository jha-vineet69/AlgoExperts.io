def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)- 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter+=1
    return array


def swap(m, n, arr):
    arr[m], arr[n] = arr[n], arr[m]


#Time Complexity: O(n^2)
#Space Complexity: O(1)
