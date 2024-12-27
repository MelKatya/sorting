from timer_dec import timer


@timer
def cocktail_sort(numbers):
    sorted_numbers = numbers[:]
    start = 0
    end = len(sorted_numbers) - 1

    while start < end:
        for i in range(start, end):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
        end -= 1

        for i in range(end, start - 1, -1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
        start += 1

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = cocktail_sort(numbers_list)
print(result_1)
print()
