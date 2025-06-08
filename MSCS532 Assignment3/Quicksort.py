import random

def randomized_partition(arr, low, high):
    # Choose a random pivot index between low and high
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Example usage:
test_arrays = [
    [],                      # Empty array
    [3, 3, 3, 3],            # All duplicates
    [1],                    # Single element
    [5, 1, 4, 2, 8, 5, 3],   # General case
    [1, 2, 3, 4, 5]          # Already sorted
]

for i, test in enumerate(test_arrays):
    arr = test.copy()
    randomized_quicksort(arr)
    print(f"Test case {i + 1}: {arr}")
