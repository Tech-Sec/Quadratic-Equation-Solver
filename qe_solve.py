try:
    import math
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    D = math.sqrt(b*b - 4 * a * c)
    d = str(D)

    print('Discriminant =' + d)
    step1 = -b + D
    step2 = step1 / 2 * a
    x1 = str(step2)
    print('x1 =' + x1)

    step3 = -b - D
    step4 = step3 / 2 * a
    x2 = str(step4)
    print('x2 =' + x2)

except ValueError:
    print('Roots are imaginary')
