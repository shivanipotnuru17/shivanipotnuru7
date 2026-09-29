def linear_search(items, key):
    for i, value in enumerate(items):
        if value == key:
            return i
    return -1

numbers = [8, 3, 11, 5]

print(linear_search(numbers, 11))
print(linear_search(numbers, 7))