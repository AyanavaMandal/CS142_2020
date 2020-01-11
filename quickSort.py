# Quick Sort
'''
- i 
6,7,4,8,2,
- - j

- - i 
6 4 7 8 2 
- - - j

- - - i
6 4 2 8 7
- - - - - j 
    p
2 4 6 8 7


i = pivot + 1 (will control the length of the short list)
j = pivot + 1 (move through the list)
6 
'''

def partition(iL, low , high):
    # choose pivot
    pivot = iL[low]
    # declare i
    i = low + 1
    # loop n-1 times (j)
    for j in range(low+1,high):
        # Compare j with pivot
        # if j < pivot
        if iL[j] < pivot:
            # swap j with i
            iL[i], iL[j] = iL[j], iL[i]
            # increase i by 1
            i = i + 1
    # swap pivot
    iL[low], iL[i-1] = iL[i-1] , iL[low]
    # return pivot position
    return (i-1)

def quickSort(iL, low , high):
    if low < high:
        # Get pivot position from partition
        pp = partition(iL, low, high)
        # Quicksort on left
        # print("Calling quickSort on left")
        quickSort(iL, low , pp)
        # quicksort on right
        # print("Calling quickSort on right")
        quickSort(iL, pp + 1 , high)
    
a = [6,5,4,3,2,1]
quickSort(a, 0, len(a))
print(a)