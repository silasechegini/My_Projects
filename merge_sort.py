#  The aim of this code is to sort the elements of an array in a more 
# efficient way that is not the bubble sort, rather, the merge sort.

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        lefttarr = dataset[:mid]
        rightarr = dataset[mid:]

        # now, recursively reduce the array size to one
        mergeSort(lefttarr)
        mergeSort(rightarr)

        # now, begin the merge operation
        i = 0 #index for the left array
        j = 0 #index for the right array
        k = 0 #index for the merged array

        # while each array has content
        while i < len(lefttarr) and j < len(rightarr):
            if lefttarr[i] < rightarr[j]:
                dataset[k] = lefttarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # now, add what ever is left of both arrays to the dataset
        while i < len(lefttarr):
            dataset[k] = lefttarr[i]
            i += 1
            k += 1
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

print(items)
mergeSort(items)
print(items)
