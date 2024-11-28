def foo(arr):
    """
    This wil have a computational complexity of O(n)
    """
    total, product = 0, 1
    for i in range(len(arr)):
        total += arr[i]
    for j in range(len(arr)):
        product *= arr[i]
    return (total, product)


def main():
    arr = [6, 5, 7, 9, 1, 3, 4]
    print(f"Total and product of the array {arr} is {foo(arr=arr)}.")
    print("This wil have a computational complexity of O(n)")


if __name__ == '__main__':
    main()
