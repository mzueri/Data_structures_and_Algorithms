
# recursive Fibonacci

def fibonacci(n:int)->int:
    assert isinstance(n,int),TypeError
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range(10):
    print(fibonacci(i))