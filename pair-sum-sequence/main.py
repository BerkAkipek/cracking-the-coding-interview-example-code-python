#!/usr/bin/python3

def pair_sum_sequence(n):
    sm = 0
    for i in range(n):
        sm = pair_sum(i, i+1)
    return sm


def pair_sum(a, b):
    return a + b


def main():
    for i in range(24):
        print(f"{i} : {pair_sum_sequence(i)}")


if __name__ == '__main__':
    main()
