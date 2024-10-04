def insertionSort(list):
    i = 1
    while i< len(list):
        itemToInsert = list[i]
        j = i-1
        while j>=0:
            if itemToInsert < list[j]:
                list[j+1] = list[j]
                j -= 1
            else:
                break
        list[j+1] = itemToInsert
        i+=1

list = [42, 17, 89, 23, 76, 58, 3, 91, 34, 68]
print(list)
insertionSort(list)
print(list)      