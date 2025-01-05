from timer_dec import timer
from typing import List, Union


@timer
def selection_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Сортировка выборкой

    Алгоритм последовательно находит наименьший элемент из оставшейся части списка
    и перемещает его в начало. Это происходит для каждой позиции в списке, начиная с первой.
    """
    sorted_numbers = numbers[:]

    for i in range(len(sorted_numbers)):
        # Считаем текущий индекс минимальным элементом в списке
        lowest_value_index = i

        # Находим индекс наименьшего элемента в оставшейся части списка
        for j in range(i + 1, len(sorted_numbers)):
            if sorted_numbers[j] < sorted_numbers[lowest_value_index]:
                lowest_value_index = j

        # Меняем местами текущий элемент с наименьшим элементом
        sorted_numbers[i], sorted_numbers[lowest_value_index] = sorted_numbers[lowest_value_index], sorted_numbers[i]

    return sorted_numbers


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = selection_sort(numbers_list)
print(result_1)
print()
