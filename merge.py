from timer_dec import timer
from typing import List, Union


def merge(left_numbers: List[Union[int, float]], right_numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Слияние двух отсортированных списков"""
    sorted_list = []

    # Сравниваем первые элементы левого и правого списка.
    # Наименьшее значение попадает в отсортированный список
    while left_numbers and right_numbers:

        if left_numbers[0] <= right_numbers[0]:
            sorted_list.append(left_numbers[0])
            left_numbers.pop(0)
        else:
            sorted_list.append(right_numbers[0])
            right_numbers.pop(0)

    # Добавляем оставшиеся элементы из левого или правого списка
    sorted_list += left_numbers
    sorted_list += right_numbers

    return sorted_list


def _merge_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Вспомогательная рекурсивная функция для сортировки слиянием"""
    if len(numbers) <= 1:
        return numbers

    # Середина списка
    middle = len(numbers) // 2

    left_list = _merge_sort(numbers[:middle])
    right_list = _merge_sort(numbers[middle:])

    return merge(left_list, right_list)


@timer
def merge_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Сортировка слиянием с использованием вспомогательной рекурсивной функции.
    Алгоритм разбивает список на подсписки, сортирует их и объединяет в один отсортированный список
    """
    sorted_numbers = numbers[:]

    return _merge_sort(sorted_numbers)


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = merge_sort(numbers_list)
print(result_1)
print()
