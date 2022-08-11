def reversed2(x):
    if len(x) == 1:
        return x
    
    return reversed2(x[1:]) + x[0]

if __name__ == "__main__":
    s = input()
    print(reversed2(s))