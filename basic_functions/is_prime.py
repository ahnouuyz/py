def is_prime(n):
    """ Check if a given number is prime.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2:
        if n % 2 == 0:
            return False
        for i2 in range(3, int(n ** 0.5) + 1, 2):
            """ Proof:
                    Let a * b = N and 1 < a <= b < N, 
                    Then a * a <= N, 
                    Thus a <= N ** 0.5
            """
            if n % i2 == 0:
                return False
        return True

def prime_factorial(n):
    """ Returns the product of all prime numbers up to the given number.
    """
    result = 1
    for i in range(2, n + 1):
        if is_prime(i):
            result *= i
    return result

def list_primes(lo, hi):
    """ Returns a list of prime numbers between the given numbers.
    """
    if lo > hi:
        lo, hi = hi, lo
    return [i for i in range(lo, hi + 1) if is_prime(i)]

def tests():
    examples = ['print(is_prime(0))', 
                'print(is_prime(1))', 
                'print(is_prime(2))', 
                'print(is_prime(60))', 
                'print(is_prime(799))', 
                'print(list_primes(50, 300))']
    for example in examples:
        print(example)
        eval(example)

if __name__ == '__main__':
    tests()
