def printUnorderedPairs(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i], arr[j])


def main():
    arr = [6, 5, 7, 9, 1, 3, 4]
    print(arr)
    print(printUnorderedPairs(arr=arr))


if __name__ == '__main__':
    main()
