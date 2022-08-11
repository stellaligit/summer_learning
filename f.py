#1 anything
n = int(input())
print('Anything:', (n * (n + 1)) // 2)

#2 loops
sum = 0
for i in range(1, n + 1):
    sum += i
print('Loops:', sum)

#3 recursion
sum = 0
def f(x):
    if x == 1:
        return 1
    return x + f(x - 1)

print('Recursion:', f(n))