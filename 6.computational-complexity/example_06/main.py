def reverse_arr(arr):
    """
    This is a destructive reverse algorithm
    It runs in O(n) time
    """
    for i in range(len(arr) // 2):
        other = (len(arr) - i - 1)
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp


def main():
    arr = [6, 5, 7, 9, 1, 3, 4]
    print(arr)
    reverse_arr(arr=arr)
    print(arr)


if __name__ == '__main__':
    main()

