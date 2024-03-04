def find_max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    elif len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    mid = len(arr) // 2

    left_max, left_min = find_max_min(arr[:mid])
    right_max, right_min = find_max_min(arr[mid:])

    max_val = max(left_max, right_max)
    min_val = min(left_min, right_min)

    return max_val, min_val


arr = [5, 8, 3, 12, 6, 2, 11]
max_val, min_val = find_max_min(arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
