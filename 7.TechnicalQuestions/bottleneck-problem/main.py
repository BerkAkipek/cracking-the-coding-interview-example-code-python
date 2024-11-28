# Example

# Given an array of distinct integer values.
# Count the number of pairs that have difference k.

# For example given the array: [1, 7, 5, 9, 2, 12, 13] and k = 2
# there are 4 pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)

# Let's try brute force approach first:

def found_pairs_with_difference(arr, k):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):    # This is bottleneck
            if abs(arr[i] - arr[j]) == k:
                result.append((arr[i], arr[j]))
    return result

# We manage to do so. It has O(N**2) computational complexity.

