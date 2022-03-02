from re import X
from tkinter import Y


def fibonacci(n):
    """
    this function takes an integar (n) and returns value of index (n) in fibonacci series
    """
    if  n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def lucas(n):
    """
    this function takes an integar (n) and returns the value of index (n) in lucas series 
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)
    
    
def sum_series (n, x=0, y=1):
    """
    this function takes an integar (n) and two optional parameters (x,y) (they are assigned to (0,1) in default), and will return the sum of the last
    two entries in the series . 

    """
    if n ==0:
       return x
    elif n==1:
        return y
    else :
        return sum_series(n-1) + sum_series(n-2)
