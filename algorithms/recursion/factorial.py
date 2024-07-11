
# recursive Factorial

def factorial(n:int)->int:
    assert isinstance(n,int)&(n>=0),TypeError("Invalid input. Make sure it is a non-negative integer.")
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

"""
for i in range(10):
    print(factorial(i))
    """
