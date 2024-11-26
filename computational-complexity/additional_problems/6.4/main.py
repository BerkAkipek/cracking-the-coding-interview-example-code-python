def div(a, b):
    """
    This function performs integer division in O(a/b) time
    """
    count = 0
    total = b
    while total <= a:
        print(total)
        total += b
        count += 1
    return count
