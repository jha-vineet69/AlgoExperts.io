def selectionSort(array):
    current = 0
    while current < len(array) - 1:
        small = current
        for i in range(current + 1, len(array)):
            if array[small] > array[current]:
                small = i
        swap(current, small, array)
        current+=1
    return array


def swap(m, n, arr):
    arr[m], arr[n] = arr[n], arr[m]



#Time Complexity: O(n^2)
#Space Complexity: O(1)