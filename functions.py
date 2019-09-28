def multiplication(first, second):
    product = first * second
    print("product = ", product)

multiplication(4, 5)

def gcd(a, b):
    while(b != 0):
        r = a
        a = b
        b = r % b
    return a


print("the greatest common denominator is ", gcd(20, 8))
