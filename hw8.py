import time
import random

N = 1000000
data = [random.randint(0, 65535) for _ in range(N)]

def counting_sort(arr):
    if not arr: return arr
    max_val = 65535
    counts = [0] * (max_val + 1)
    
    for x in arr:
        counts[x] += 1
        
    sorted_arr = []
    for num, count in enumerate(counts):
        sorted_arr.extend([num] * count)
    return sorted_arr

def radix_sort_16bit(arr):
    def counting_sort_for_radix(input_arr, shift):
        counts = [[] for _ in range(256)]
        for x in input_arr:
            bucket_idx = (x >> shift) & 0xFF
            counts[bucket_idx].append(x)
        
        output_arr = []
        for bucket in counts:
            output_arr.extend(bucket)
        return output_arr

    arr = counting_sort_for_radix(arr, 0)
    arr = counting_sort_for_radix(arr, 8)
    return arr

start = time.time()
res_builtin = sorted(data)
print(f"Python sorted(): {time.time() - start:.4f} s")

start = time.time()
res_counting = counting_sort(data)
print(f"Counting Sort: {time.time() - start:.4f} s")

start = time.time()
res_radix = radix_sort_16bit(data)
print(f"Radix Sort: {time.time() - start:.4f} s")
