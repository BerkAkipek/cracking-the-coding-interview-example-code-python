def printUnorderedPairs(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            if arrA[i] < arrB[j]:
                print(arrA[i], arrB[j])


def main():
    arrA = [6, 5, 7, 9, 1, 3, 4]
    arrB = [7, 8, 5, 9, 1, 4, 5]
    print(f"arrayA: {arrA} | arrayB: {arrB}")
    printUnorderedPairs(arrA=arrA, arrB=arrB)


if __name__ == '__main__':
    main()
