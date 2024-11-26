def recurring_sum(n):
    """
    This function has a time complexity of O(2**n) and O(n) space complexity.
    """
    if n <= 1:
        return 1
    return recurring_sum(n-1) + recurring_sum(n-1)


def main():
    for i in range(16):
        print(f"Recurring sum of 4: {recurring_sum(i)}")
    print("This function has a time complexity of O(2**n) and O(n) space complexity.")


if __name__ == '__main__':
    main()
