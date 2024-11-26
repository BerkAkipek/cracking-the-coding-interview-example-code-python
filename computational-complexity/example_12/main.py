def permutation(string, prefix):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i+1:]
            permutation(rem, prefix + string[i])


def main():
    arr = ['a', 'ab', 'abc', 'abcd', 'abcde']
    for string in arr:
        print(f"For string: {string}")
        permutation(string, "")


if __name__ == '__main__':
    main()
