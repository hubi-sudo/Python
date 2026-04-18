def is_prime(num):
    if num == 1:
        print(False)
    else:
        i = 1
        dzielniki = []
        for i in range(1,num+1):
            if num%i == 0:
                dzielniki.append(i)
        if len(dzielniki) > 2:
            print(False)
        else:
            print(True)

is_prime()
