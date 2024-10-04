def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def partition(list, left, right):
    middle = (left+right)//2
    pivot = list[middle]
    list[middle] = list[right]
    list[right] = pivot
    boundary = left
    for index in range(left,right):
        if list[index] < pivot:
            swap(list, index, boundary)
            boundary += 1
    swap(list, right, boundary)
    return boundary

def quickSortHelper(list, left, right):
    if left<right:
        pivotLocation = partition(list, left, right)
        quickSortHelper(list, left, pivotLocation-1)
        quickSortHelper(list, pivotLocation+1, right)

def quickSort(list):
    quickSortHelper(list, 0, len(list)-1)

list = [42, 17, 89, 23, 76, 58, 3, 91, 34, 68]
print(list)
quickSort(list)
print(list)      