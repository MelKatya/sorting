from timer_dec import timer


@timer
def insertion_sort(numbers):
    sorted_numbers = numbers[:]

    for i in range(1, len(sorted_numbers)):
        value = sorted_numbers[i]
        index = i

        while index > 0 and sorted_numbers[index - 1] > value:
            sorted_numbers[index] = sorted_numbers[index - 1]
            index -= 1

        sorted_numbers[index] = value

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = insertion_sort(numbers_list)
print(result_1)
print()
