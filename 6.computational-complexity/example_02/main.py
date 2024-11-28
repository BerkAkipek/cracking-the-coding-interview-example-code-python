def printPairs(arr):
    """
    This has a computational complexity of O(N**2)
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


def main():
    arr = [6, 5, 7, 9, 1, 3, 4]
    print(arr)
    printPairs(arr=arr)


if __name__ == '__main__':
    main()
