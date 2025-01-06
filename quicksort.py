from timer_dec import timer
from typing import List, Union


def _quick_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Вспомогательная функция для быстрой сортировки
    """
    # Базовый случай рекурсии
    if len(numbers) <= 1:
        return numbers

    # Опорный элемент (средний элемент списка)
    pivot = numbers[len(numbers) // 2]

    # Разбиение списка на три части
    # Элементы меньше опорного
    left = [num for num in numbers if num < pivot]
    # Элементы равные опорному
    middle = [num for num in numbers if num == pivot]
    # Элементы больше опорного
    right = [num for num in numbers if num > pivot]

    # Рекурсивная сортировка и объединение результата
    return _quick_sort(left) + middle + _quick_sort(right)


@timer
def quick_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Быстрая сортировка

    Делит список на три части (меньше, равно, больше опорного элемента),
    рекурсивно сортирует "меньшие" и "большие" части, а затем объединяет их
    """
    sorted_numbers = numbers[:]

    # Запуск вспомогательной рекурсивной функции
    return _quick_sort(sorted_numbers)


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result = quick_sort(numbers_list)
print(result)
