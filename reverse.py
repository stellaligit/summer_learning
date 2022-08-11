def reverse(x):
    if len(x) == 1:
        return x
    
    return x[-1] + reverse(x[:-1])

s = input()
print(reverse(s))