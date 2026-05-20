def fatorial(n, show=False):
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i}', end=' ')
            if i>1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= i
    
    return f


print(fatorial(5, True))
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print(fatorial(10, False))
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print(fatorial(10, True))
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
print(fatorial(7))
print('-=-=-=-=-=-=-=-=-=-=-=-=-')

