from timer_dec import timer


@timer
def bubble_sort_classic(numbers):
    sorted_numbers = numbers[:]
    for i in range(len(sorted_numbers)):
        for j in range(len(sorted_numbers) - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    return sorted_numbers


@timer
def bubble_sort_swapped(numbers):
    sorted_numbers = numbers[:]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True
    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = bubble_sort_classic(numbers_list)
print(result_1)
print()

result_2 = bubble_sort_swapped(numbers_list)
print(result_2)
