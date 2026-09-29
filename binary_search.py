def binary_search(items, key):
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == key:
            return mid

        if items[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [2, 4, 6, 8, 10]

print(binary_search(numbers, 8))
print(binary_search(numbers, 9))