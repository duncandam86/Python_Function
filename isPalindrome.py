def isPalindrome (string):
    '''this function to check if a string of words is palindrome or not'''
    reversed_string = string[::-1]
    if reversed_string == string:
        print ('this is  Palindrome')
    else:
        print ('not a Palindrome')

isPalindrome('boob')