def sqrt(n):
    """
    This algorithm computes sqrt of n if n is a perfect square -1 otherwise.
    This algorith has O(sqrt(n)) time.
    """
    guess = 1
    while guess * guess <= n:
        if guess * guess == n:
            return n
        guess += 1
    return -1

