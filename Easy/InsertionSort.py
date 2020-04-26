def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j>0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j-=1
    return array

def swap(m, n, arr):
    arr[m], arr[n] = arr[n], arr[m]


#Time Complexity: O(n^2)
#Space Complexity: O(1)
