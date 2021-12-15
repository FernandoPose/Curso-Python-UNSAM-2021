# Ejercicio 11.9

def pascal(n, k):
    if (n == k) or (k == 0):
        return 1
    res = pascal(n-1, k-1) + pascal(n-1, k)
    return res

def main():
    print(pascal(5, 2))

if __name__ == '__main__':
    main()