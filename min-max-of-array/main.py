import math


def min_max(arr):
    mn = math.inf
    mx = -math.inf
    for element in arr:
        if element < mn:
            mn = element
        if element > mx:
            mx = element
    return (mn, mx)


def main():
    arr = [6, 5, 7, 9, 1, 3, 4]
    print(f"Min and maximum of array {arr} is {min_max(arr)}")


if __name__ == '__main__':
    main()
