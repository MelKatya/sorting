from timer_dec import timer


@timer
def selection_sort(numbers):
    sorted_numbers = numbers[:]

    for i in range(len(sorted_numbers)):
        lowest_value_index = i

        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[j] < sorted_numbers[lowest_value_index]:
                lowest_value_index = j

        sorted_numbers[i], sorted_numbers[lowest_value_index] = sorted_numbers[lowest_value_index], sorted_numbers[i]

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = selection_sort(numbers_list)
print(result_1)
print()
