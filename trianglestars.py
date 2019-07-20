def triangleStars(k):
    '''this function produce the number of row with * in triangle format'''
    for x in range (k):
        print(' ' *(k-x-1) + '*' *(2*x+1))

triangleStars(9)