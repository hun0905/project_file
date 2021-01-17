n = input()
n = int(n)
for i in range(n):
    A = input('\n')
    F = input()
    A = int(A)
    F = int(F)
    print()
    for j in range(F):
        for k in range(A):
            print(f'{k+1}'*(k+1))
        for k in range(A,1,-1):
            print(f'{k-1}'*(k-1))
        print()