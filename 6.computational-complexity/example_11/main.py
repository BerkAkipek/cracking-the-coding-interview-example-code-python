def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    for i in range(12):
        print(f"{i} : {factorial(i)}")


if __name__ == '__main__':
    main()
