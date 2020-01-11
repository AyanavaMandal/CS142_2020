# Bubble Sort
def BubbleSort(inputList):
    # Code for n passes
    # Loop n times : Length of the input list
    for i in range(len(inputList)):
        # Code for 1 pass
        # Loop n - 1 times
        for j in range(len(inputList)-1):
            # Check if violation 
            if inputList[j] > inputList[j+1]:
                # Swap
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
            # Shift the window (Covered in (j) for loop)
    return inputList

a = [6,5,4,3,2,1]
print(BubbleSort(a))