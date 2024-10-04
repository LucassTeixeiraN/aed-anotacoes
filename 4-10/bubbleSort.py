def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubbleSortWithTweak(list):
    n=len(list)
    while n>1:
        swapped = False
        i = 1
        while i< n:
            if list[i] < list[i-1]:
                swap(list, i, i-1)
                swapped = True
            i+=1
        if not swapped: break
        n-=1

list = [42, 17, 89, 23, 76, 58, 3, 91, 34, 68]
print(list)
bubbleSortWithTweak(list)
print(list)      