# Counting Sort
def counting_sort(arr):
    biggest = max(arr)
    count = [0] * (biggest + 1)

    for num in arr:
        count[num] = count[num] + 1

    result = []

    for num in range(biggest + 1):
        while count[num] > 0:
            result.append(num)
            count[num] = count[num] - 1

    return result

data = [4, 2, 2, 8, 3, 3, 1]
print("Before sorting:", data)
result = counting_sort(data)
print("After sorting: ", result)