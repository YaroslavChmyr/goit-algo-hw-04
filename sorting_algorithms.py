import random
import timeit


# Сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst


# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Створюємо набори даних

small_arr = [random.randint(0, 1000) for _ in range(100)]
large_arr = [random.randint(0, 1000) for _ in range(1000)]


# Проводимо емпіричне вимірювання

measured_mer1 = timeit.timeit(lambda: merge_sort(small_arr.copy()), number=10)
measured_ins1 = timeit.timeit(lambda: insertion_sort(small_arr.copy()), number=10)
measured_sort1 = timeit.timeit(lambda: sorted(small_arr.copy()), number=10)

measured_mer2 = timeit.timeit(lambda: merge_sort(large_arr.copy()), number=10)
measured_ins2 = timeit.timeit(lambda: insertion_sort(large_arr.copy()), number=10)
measured_sort2 = timeit.timeit(lambda: sorted(large_arr.copy()), number=10)

# Виводимо результати

print(f"Результати для меншого набору даних:\nЧас виконання сортування злиттям - {measured_mer1}\nЧас виконання сортування вставками - {measured_ins1}\nЧас виконання сортування Timsort - {measured_sort1}")
print(f"\nРезультати для більшого набору даних:\nЧас виконання сортування злиттям - {measured_mer2}\nЧас виконання сортування вставками - {measured_ins2}\nЧас виконання сортування Timsort - {measured_sort2}")


