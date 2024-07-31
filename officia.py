def in_range(arr, min_val, max_val):
    for num in arr:
        if not min_val <= num <= max_val:
            return False
    return True
