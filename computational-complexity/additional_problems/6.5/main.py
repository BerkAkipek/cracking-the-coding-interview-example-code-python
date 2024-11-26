def sqrt(n):
    """
    Returns square root of n if n is a perfect square number.
    This algorithm runs O(log(n)) times.
    """
    return sqrt_helper(n, 1, n)


def sqrt_helper(n, mn, mx):
    if mx < mn: return -1
    guess = (mn + mx) // 2 
    if guess * guess == n:
        return guess
    elif guess * guess < n:
        return sqrt_helper(n, guess + 1, mx)
    else:
        return sqrt_helper(n, mn, guess - 1)
    

def main():
    for i in range(24):
        print(f"{i}: {sqrt(i)}")


if __name__ == '__main__':
    main()
