"""
    my_doctest 2018-09-05
"""
def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0


    """
    assert type(n) == int, 'n is not int type'

    return n if n>0 else (-n)
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n should larger than 0
    '''
    if n < 0:
        raise ValueError(r"n should larger than 0")
    elif n <= 1:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(__doc__)
    print(fact.__name__)
    abs(123)
