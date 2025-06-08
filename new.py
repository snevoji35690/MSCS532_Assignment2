
import time
import random
import tracemalloc

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Quick Sort
def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pivot_index = partition(items, low, high)
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low
        for j in range(low, high):
            if items[j] <= pivot:
                items[i], items[j] = items[j], items[i]
                i += 1
        items[i], items[high] = items[high], items[i]
        return i

    _quick_sort(arr, 0, len(arr) - 1)

# Benchmarking
def benchmark(sort_func, data):
    tracemalloc.start()
    start_mem = tracemalloc.get_traced_memory()[0]
    start_time = time.perf_counter()

    sort_func(data.copy())

    end_time = time.perf_counter()
    end_mem = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()

    time_taken = (end_time - start_time) * 1000  # ms
    memory_used = (end_mem - start_mem) / 1024   # KB
    return round(time_taken, 2), round(memory_used, 2)

# Dataset
size = 10000
sorted_data = list(range(size))
reverse_sorted_data = list(range(size, 0, -1))
random_data = random.sample(range(size * 2), size)

datasets = {
    "Sorted": sorted_data,
    "Reverse Sorted": reverse_sorted_data,
    "Random": random_data
}

print(f"{'Algorithm':<12} {'Input Type':<16} {'Time (ms)':<12} {'Memory (KB)'}")
print("-" * 50)

for name, dataset in datasets.items():
    time_ms, mem_kb = benchmark(merge_sort, dataset)
    print(f"{'Merge Sort':<12} {name:<16} {time_ms:<12} {mem_kb}")

    time_ms, mem_kb = benchmark(quick_sort, dataset)
    print(f"{'Quick Sort':<12} {name:<16} {time_ms:<12} {mem_kb}")
