def fibonnaciSeries(x):
    ''' this function to create the fibonnaci series with total number of x in the series'''
    a = int(x)
    f = 0
    s = 1
    if a <= 0:
        print('The fibonnaci series is ', f)
    else: 
        print ('The fibonnaci series is ', f, s,end = '')
        for _ in range (2,a):
            next_num = f+s
            print ('', next_num, end = ' ')
            f = s
            s = next_num

fibonnaciSeries(6)