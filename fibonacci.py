'''
#RealCode
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 25):
    print(fibonacci(i))
'''

#StackOverflow!
def fibonacci(n):
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 25):
    print(fibonacci(i))