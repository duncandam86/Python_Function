def kthlargest (arr,k):
    ''' this function can be used to find the k largest numbers in an array'''
    n = len(arr)
    if k < n:
        arr.sort(reverse = True)
        for i in range(k):
            print(arr[i])
    else:
        print('Not possible')


arr2 = [22,13,15,18,19,22,24,26,28,30,44]
k2= 5
kthlargest(arr2,k2)