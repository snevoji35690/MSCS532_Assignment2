
import random
import time
import tracemalloc

# ----------------- Merge Sort -----------------
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

# ----------------- Quick Sort -----------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

# ----------------- Performance Testing -----------------
def measure_performance(sort_func, data):
    tracemalloc.start()
    start_time = time.perf_counter()
    sorted_data = sort_func(data)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024, sorted_data  # Time in seconds, memory in KB

# ----------------- Test Datasets -----------------
def generate_datasets(size):
    random_data = random.sample(range(size * 2), size)
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted_data[::-1]
    return random_data, sorted_data, reverse_sorted_data

# ----------------- Main Execution -----------------
if __name__ == "__main__":
    size = 1000  # You can increase for more intensive testing
    datasets = generate_datasets(size)
    labels = ["Random", "Sorted", "Reverse Sorted"]
    
    print(f"{'Dataset':<20} {'Algorithm':<15} {'Time (s)':<10} {'Memory (KB)':<12}")
    print("-" * 60)

    for label, data in zip(labels, datasets):
        for sort_func, name in [(merge_sort, "Merge Sort"), (quick_sort, "Quick Sort")]:
            time_taken, mem_usage, _ = measure_performance(sort_func, data.copy())
            print(f"{label:<20} {name:<15} {time_taken:<10.6f} {mem_usage:<12.2f}")


