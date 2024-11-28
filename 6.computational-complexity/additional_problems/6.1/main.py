def product(a, b):
    """
    Calculates a * b in O(b) time
    """
    total = 0
    for i in range(b):
        total += a
    return total
