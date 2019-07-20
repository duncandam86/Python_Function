def isPrime (x):
    '''This function to check if the number is a prime'''
    if x > 1:
        for y in range(2,x):
            if (x%y) == 0:
                print(x, "it's not a prime")
                break
            else:
                print (x, "it's a prime")
                break
    else:
        print (x, "it's not a prime")

isPrime(121)

