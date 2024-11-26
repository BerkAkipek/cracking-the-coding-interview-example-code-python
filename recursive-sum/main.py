#!/usr/bin/python3

def recursive_sum(n):
    """
    Recursive Sum of all positive numbers until n
    """
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n-1)
    

def main():
    sm = recursive_sum(36)
    print(f"Sum of all numbers until 37 is {sm}.")


if __name__ == '__main__':
    main()
