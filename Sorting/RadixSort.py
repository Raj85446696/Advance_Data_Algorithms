def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    # Count digit occurrences
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Convert count[] to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (right to left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Test the code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted Array:", arr)
