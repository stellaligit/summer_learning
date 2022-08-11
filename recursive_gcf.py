from pyrsistent import T


def gcd (m, n):
    a = max(m, n)
    b = min(m, n)
    t = a % b
    if t == 0:
        return b
    else:
        return gcd (b, t)