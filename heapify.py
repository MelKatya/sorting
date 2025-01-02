from timer_dec import timer


@timer
def heap_sort(numbers):
    sorted_numbers = numbers[:]

    for i in range(len(sorted_numbers), -1, -1):
        heapify(sorted_numbers, len(sorted_numbers), i)

    for i in range(len(sorted_numbers) - 1, 0, -1):
        sorted_numbers[i], sorted_numbers[0] = sorted_numbers[0], sorted_numbers[i]
        heapify(sorted_numbers, i, 0)

    return sorted_numbers


def heapify(numbers, heap_size, root_index):
    max_num_index = root_index
    left = max_num_index * 2 + 1
    right = max_num_index * 2 + 2

    if left < heap_size and numbers[left] > numbers[max_num_index]:
        max_num_index = left

    if right < heap_size and numbers[right] > numbers[max_num_index]:
        max_num_index = right

    if max_num_index != root_index:
        numbers[root_index], numbers[max_num_index] = numbers[max_num_index], numbers[root_index]
        heapify(numbers, heap_size, max_num_index)




numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = heap_sort(numbers_list)
print(result_1)
print()
