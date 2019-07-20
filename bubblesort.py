def bubblesort(arr):
    '''this function can be used to sort an array using bubble sort algorith'''
    size = len(arr)
    #travel through all array in elements
    for x in range(size-1):
        #last elements are already in the place
        for y in range (0, size - x -1):
            #swap the elements if found it's greater
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    print(arr)

arr = [5,9,12,11,0,4,8,10]
arr2 = [2,5,10101,12232,102,445,123,2993,2019]

bubblesort(arr)
bubblesort(arr2)