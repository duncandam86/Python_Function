def convertStringtoNum(string):
    ''' this function convert a string of numbers into a integer'''
    value = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    number = 0
    for digit in string:
        number =  10*number + value[digit]
    print(number)
    
convertStringtoNum('123')