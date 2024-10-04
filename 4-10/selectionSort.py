def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def selectionSort(list):
    i = 0
    while i<len(list) - 1:
        minIndex = i
        j = i+1
        while j < len(list):
            if list[j] < list[minIndex]:
                minIndex = j
            j += 1

        if minIndex != i:
            swap(list, minIndex, i)
        i += 1

list = [42, 17, 89, 23, 76, 58, 3, 91, 34, 68]
print(list)
selectionSort(list)
print(list)        