def powers_of_2(n):
    """
    Prints the powers of 2 until n.
    It has a computational complexity of O(log(n))
    """
    if  n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powers_of_2(n//2)
        curr = prev * 2
        print(curr)
        return curr
    

def main():
    powers_of_2(1021)


if __name__ == '__main__':
    main()
