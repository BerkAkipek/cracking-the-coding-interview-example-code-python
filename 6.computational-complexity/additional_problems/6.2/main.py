def power(a, b):
    """
    Calculates a**b in O(b) time.
    """
    if b < 0: return 0
    elif b == 0: return 1
    else: return a * power(a, b-1)
