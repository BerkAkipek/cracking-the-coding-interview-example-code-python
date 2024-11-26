#!/usr/bin/python3

def iterative_sum(n):
    result = 0
    for i in range(n):
        result += (i + 1)
    return result


def main():
    sm = iterative_sum(36)
    print(f"Sum of all numbers until 37 is {sm}.")


if __name__ == '__main__':
    main()
