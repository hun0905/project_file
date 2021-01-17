n = True
num_s = ''
while n != False:
    n = input()
    n = int(n)
    while n != 0:
        num_s = str(n%2) + num_s 
        n //= 2
    print(num_s)
    num_s = ''