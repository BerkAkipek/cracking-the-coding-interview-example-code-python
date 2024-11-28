def isPrime(n):
    """
    Returns True if the number n is a prime
    It runs O(sqrt(N)) times
    """
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def main():
    for i in range(2, 36):
        print(f"{i} | isPrime: {isPrime(i)}")


if __name__ == '__main__':
    main()
