def mod(a, b):
    """
    Calculates the remainder of a/b.
    This function has O(1) time.
    """
    if b < 0: return -1
    div = a // b
    return a - div * b


def main():
    for i in range(12):
        print(f"{i}: {mod(i, 3)}")


if __name__ == '__main__':
    main()
