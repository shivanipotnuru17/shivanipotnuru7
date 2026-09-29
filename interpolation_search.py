def interpolation_search(a, key):
    low, high = 0, len(a) - 1

    while low <= high and a[low] <= key <= a[high]:
        if a[low] == a[high]:
            return low if a[low] == key else -1

        pos = low + (key - a[low]) * (high - low) // (a[high] - a[low])

        if a[pos] == key:
            return pos

        if a[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1

print(interpolation_search([10, 20, 30, 40, 50], 40))
print(interpolation_search([10, 20, 30, 40, 50], 35))