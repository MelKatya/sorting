from typing import List, Union
from timer_dec import timer


@timer
def heap_sort(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Пирамидальная сортировка (сортировка кучей).

    Алгоритм сначала строит максимальную кучу (heap), а затем
    постепенно извлекает наибольший элемент, переставляя его в конец списка.
    """
    sorted_numbers = numbers[:]
    len_list = len(sorted_numbers)

    # Построение максимальной кучи
    for i in range(len_list // 2, -1, -1):
        heapify(sorted_numbers, len(sorted_numbers), i)

    # Извлечение элементов из кучи
    for i in range(len_list - 1, 0, -1):
        # Меняем корень (максимальный элемент) с последним элементом
        sorted_numbers[i], sorted_numbers[0] = sorted_numbers[0], sorted_numbers[i]
        # Восстанавливаем кучу для оставшейся части
        heapify(sorted_numbers, i, 0)

    return sorted_numbers


def heapify(numbers: List[int, float], heap_size: int, root_index: int) -> None:
    """Преобразование поддерева в кучу с корнем в 'root_index'"""
    # Индекс наибольшего элемента (изначально считаем, что это корневой индекс)
    max_num_index = root_index
    # Левая сторона корня
    left = max_num_index * 2 + 1
    # Правая сторона корня
    right = max_num_index * 2 + 2

    # Если левая сторона - допустимый индекс и элемент больше, чем при корневом индексе
    if left < heap_size and numbers[left] > numbers[max_num_index]:
        max_num_index = left

    # То же самое для правого дочернего узла
    if right < heap_size and numbers[right] > numbers[max_num_index]:
        max_num_index = right

    # Если наибольший элемент не корень, меняем их местами
    if max_num_index != root_index:
        numbers[root_index], numbers[max_num_index] = numbers[max_num_index], numbers[root_index]
        # Рекурсивно преобразуем поддерево
        heapify(numbers, heap_size, max_num_index)


numbers_list = [1, 2, 10, 1500, -5, 0, 78, -9] * 100

result_1 = heap_sort(numbers_list)
print(result_1)

