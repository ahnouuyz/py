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
