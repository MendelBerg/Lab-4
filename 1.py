def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


def binary_search(arr, low, high, element):
    if high >= low:
        mid = (high + low) // 2
        return mid if arr[mid] == element \
            else binary_search(arr, low, mid - 1, element) \
            if arr[mid] > element \
            else binary_search(arr, mid + 1, high, element)

    return -1


ar = [2, 3, 4, 10, 40]
print('Linear: ', linear_search(ar, 40))
print('Binary: ', binary_search(ar, 0, len(ar) - 1, 40))
