def sum_digits(n):
    """
    Returns the sum of all digits in a number has O(logN) time.
    """
    total = 0
    while n > 0:
        total += n % 10
        n /= 10
    return total
