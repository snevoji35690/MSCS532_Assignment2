# merge_sort.py

def merge_sort(arr):
    """
    Sorts the input list using Merge Sort.
    Returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])             # Recursively sort left half
    right = merge_sort(arr[mid:])            # Recursively sort right half
    return _merge(left, right)


def _merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged